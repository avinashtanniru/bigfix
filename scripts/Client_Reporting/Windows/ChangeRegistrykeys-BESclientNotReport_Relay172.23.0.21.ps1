#Load list of servers below from desktop\bigfix-client-test
$AllcomputerList =  Get-Content -Path "$Home\desktop\bigfix-client-test\servers.txt"

#Total no of Servers in list
$Length = $AllcomputerList.Length
$i = 1


$StorageBOX = @()

foreach ($Computers in $AllcomputerList)
{
    Write-host "------------------------------------------------------" -ForegroundColor Yellow
    Write-host "Connecting to $computers $i /$Length" -ForegroundColor Green

    $i++
    $Table = "" | Select ComputerName, Status
    $Table.ComputerName = $Computers

    Try{
        
        $ErrorActionPreference = "stop"
        
        #Connect remote server registry and RelaySelect_Automatic - Updated
        $reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', $computers)
        $regKey=$reg.OpenSubKey("SOFTWARE\\Wow6432Node\\BigFix\\EnterpriseClient\\Settings\\Client\\__RelaySelect_Automatic",$true)
        $regKey.SetValue("value","0",[Microsoft.Win32.RegistryValueKind]::String)
        Write-Output "RelaySelect_Automatic - Updated"

        #Configure __RelayServer1 details in registry
        $reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', $computers)
        $regKey=$reg.OpenSubKey("SOFTWARE\\Wow6432Node\\BigFix\\EnterpriseClient\\Settings\\Client\\__RelayServer1",$true)
        $regKey.SetValue("value","http://172.23.0.21:52311/bfmirror/downloads",[Microsoft.Win32.RegistryValueKind]::String)
        Write-Output "__RelayServer1 - Updated"

        #Configure __Relay_Control_Server1 details in registry
        $reg = [Microsoft.Win32.RegistryKey]::OpenRemoteBaseKey('LocalMachine', $computers)
        $regKey=$reg.OpenSubKey("SOFTWARE\\Wow6432Node\\BigFix\\EnterpriseClient\\Settings\\Client\\__Relay_Control_Server1",$true)
        $regKey.SetValue("value","http://172.23.0.21:52311",[Microsoft.Win32.RegistryValueKind]::String)
        Write-Output "__Relay_Control_Server1 - Updated"

        $status = "Reg Key Updated Success"
        Write-Output $status

        #Restart BESClient service 
        Get-Service -ComputerName $computers -Name BESClient | Stop-Service -verbose
        Get-Service -ComputerName $computers -Name BESClient | Start-Service -verbose
        $Table.Status = "Success" 

        }
        Catch
        {
            Write-host "Failed to Change registrykeys" -ForegroundColor red
            $Table.Status = "Failed" 
        }
        
        #Storage computername and its status details in Storage box
        $StorageBOX += $Table
}

#display Table on the screen
$StorageBOX | Sort-Object Status -Descending 

#Save completion log file data in Logfile
$StorageBOX | Sort-Object Status -Descending | Out-File -FilePath "$Home\desktop\bigfix-client-test\Log_Status.txt"