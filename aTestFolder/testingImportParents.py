import sys
from pathlib import Path

Funsies = Path("__file__").resolve().parent / "Funsies/functioning"
sys.path.append(str(Funsies))
from funniFunctionsToNeverCall import amHateSpeech # type: ignore

amHateSpeech()