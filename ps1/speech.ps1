# Script for repeatedly saying weird things

$Phrase = "uhu";

Add-Type -AssemblyName System.Speech
$SpeechSynth = New-Object System.Speech.Synthesis.SpeechSynthesizer

function Say-Something {
    $SpeechSynth.Speak($Phrase)
}

while(1)
{
    Say-Something

    $Interval = Get-Random -Minimum 120 -Maximum 3600
    Start-Sleep -s $Interval
}
