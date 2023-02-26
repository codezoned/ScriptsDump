### Check Server Start Up Date ###
### Server UpTime ###

##Method 1
systeminfo.exe | find "System Boot Time"

Write-Host -ForegroundColor green "WIM Uptime"

##Method 2
function GetUptime {
	Param ($server)
	Try {
		$win32_os = Get-WmiObject Win32_OperatingSystem -ComputerName $server -ErrorAction Stop
		 
		# Convert to date times
		$local = $win32_os.ConvertToDateTime($win32_os.LocalDateTime)
		$boot = $win32_os.ConvertToDateTime($win32_os.LastBootUpTime)
		 
		# Calculate the uptime and return it
		$uptime = ($local - $boot)
		}
	Catch {
		$uptime = "" | Select-Object Days
		$uptime.Days = "$error[0].exception.message"
	}
	Finally { $uptime }
}
GetUptime localhost
