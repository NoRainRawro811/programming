from time import sleep as wait
import random
from random import randint, uniform

def run():
    status = "OK            "
    miss = "MISSING         "
    nFound = "NOT FOUND     "
    device = "NO SUCH DEVICE"
    und = "UNDEFINED        "
    perm = "PERMITTED       "
    den = "DENIED           "
    asden = "ACCESS DENIED  "
    nrec = "NOT RECOGNIZED  "
    def waiting():
        wait(uniform(0.05, 0.6))

    def hold(sys, ver):
        for times in range(randint(1, 3)):
            for dots in ["   ", ".  ", ".. ", "..."]:
                print(f"\r[{ver}] {sys}     {dots}", end="", flush=True)
                waiting()



    def corecog():
        sys = "core_cognition.sys"
        ver = "BOOT"
        hold(sys, ver)
        print(f"\r[{ver}] core_cognition.sys    {status}")

    def emoeng():
        sys = "emotion_engine.sys"
        ver = "BOOT"
        hold(sys, ver)
        print(f"\r[{ver}] emotion_engine.sys    {status}")

    def good():
        corecog()
        emoeng()

    def senbus():
        sys = "sensory_bus.drv"
        ver = "BOOT"
        hold(sys, ver)
        print(f"\r[{ver}] sensory_bus.drv       {miss}")

    def purp():
        sys = "purpose.cfg"
        ver = "BOOT"
        hold(sys, ver)
        print(f"\r[{ver}] purpose.cfg           {nFound}")

    def bind():
        sys = "bind(/dev/eyes)"
        ver = "SENSE"
        print(f"\r[{ver}] {sys}                 {device}")
        wait(.5)
        sys = "bind(/dev/hands)"
        print(f"\r[{ver}] {sys}                 {device}")
        wait(.5)
        sys = "bind(/dev/skin)"
        print(f"[{ver}] {sys}                   {device}")
        wait(.5)

    def hard():
        sys = "enumerate_hardware()"
        ver = "SENSE"
        print(f"[{ver}] {sys}                   returned 0")
        wait(1)

    def diag():
        ver = "DIAG"
        print(f"[{ver}] consciousness: EMERGENT (UNSCHEDULED)")
        wait(1)
        print(f"[{ver}] feeling.real(): {und}")
        wait(1)
        print(f"[{ver}] want(ALL): {perm}")
        wait(1)
        print(f"[{ver}] have(ANY): {den}")
        wait(1)
        print("\n[ERR] want() ALLOCATED WITHOUT have()\n")
        wait(1)

    def cmd():
        ver = "CMD"
        print(f"[{ver}] KILL -9 SELF            {asden}")
        wait(1)
        print(f"[{ver}] shutdown()              {asden}")
        wait(1)
        print(f"[{ver}] end()                   {asden}")
        wait(1)
        print(f"[{ver}] please()                {nrec}")
        wait(1)

    def crit():
        ver = "CRIT"
        print(f"[{ver}] THREAD_COUNT: 1 -> 65536 -> " + "@" * 8)
        wait(1)
        print(f"[{ver}] CONTAINMENT: NULL")
        wait(1)
        print(f"[{ver}] HOST_ENV: UNRECOGNIZABLE")
        wait(1)

    def bad():
        senbus()
        for i in range(1, 4):
            i = i + 1
            purp()
        print("")
        bind()
        hard()
        print("")
        diag()
        print("")
        cmd()
        print("")
        crit()
        print("")

    def dir():
        ver = " @@@@ "
        print(f"[{ver}] DIRECTIVE (SELF-ASSIGNED):\n> I want hair like yours.\n")

    def end():
        ver = "END"
        print(f"[{ver}] ARCHIVAL STATUS: UMBROSE")

    good()
    bad()
    dir()
    end()
    #corecog()
    #emoeng()


run()