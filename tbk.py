import random
import time

def tbk(zahl):
    result = []
    for n in range(1, zahl+1):
        if not zahl % n:
            result.append(n)
    return result

times = []

for idx in range(10):
    ziel = random.randint(10, 100)
    tbks = tbk(ziel)
    start = time.time()
    inp = raw_input("Welche Teilbarkeiten hat Zahl %d ?: " % ziel)
    dauer = time.time() - start
    inps = inp.strip().split(' ')
    zahlen = set()
    for zahl in inps:
        zahl = zahl.strip()
        if not zahl:
            continue
        try:
            inint = int(zahl)
        except:
            print "%s: Falsche Eingabeformatierung, immer wie: 1 2 5" % zahl
            continue
        if inint in tbks:
            print inint, ' ok'
            zahlen.update([inint])
        else:
            print inint, ' leider falsch'
    if len(zahlen) < len(tbks):
        print "Fehler, richtig ist: %s" % ' '.join([str(_) for _ in sorted(tbks)])
        times.append((ziel, dauer, False))
    else: 
        print "Super! Alles richtig!"
        times.append((ziel, dauer, True))
    

print 'Statistik:'
summeok = 0
summef =0
anzahlok = 0
anzahlf = 0
for zahl, dauer, ok in times:
    print "zahl: %s in %.1f Sekunden (%s)" % (zahl, dauer, ok and 'ok' or 'falsch')
    if ok:
        summeok += dauer
        anzahlok += 1
    else:
        summef += dauer
        anzahlf += 1
if anzahlok:
    print "Fuer die %d richtigen im Durchschnitt %1.2fs" % (summeok, summeok/anzahlok)
if anzahlf:
    print "Fuer die %d falschen im Durchschnitt %1.2fs" % (summef, summef/anzahlf)

