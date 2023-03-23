<?php
$naam = $_POST['naam'];
$achternaam = $_POST['achternaam'];
$functie = $_POST['functie'];

// Build the command to execute the PowerShell script
$command = "powershell.exe -ExecutionPolicy Bypass -File 'C:\xampp\htdocs\orc\open-chrome.ps1'";

// Pass the variables as arguments to the PowerShell script
$arguments = "-naam '$naam' -achternaam '$achternaam' -functie '$functie'";

// Combine the command and arguments
$fullCommand = "$command $arguments";

// Execute the PowerShell script
$output = shell_exec($fullCommand);

// Print the output (for debugging purposes)
echo "<pre>$output</pre>";
?>