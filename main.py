
import bot as c
import timer as t
import cProfile
import pstats
timer = t.CodeTimer() 
clicker = c.Clicker()  # Clicker object
clicker.giveCookies(1000)
def main():
    with cProfile.Profile() as pr:
        timer.codeBegining()
        clicker.ChooseBuilding()
        clicker.getUpgrade()
        clicker.clickCookie()
        clicker.ShimmerLogic()
        
        timer.codeEnd()
        print(f"Code exectued in {timer.getCodeTime():1.2f}")
    #stats = pstats.Stats(pr)
    #stats.sort_stats(pstats.SortKey.TIME)
    #stats.dump_stats(filename="profling.prof") Just testing functions please ignore ty



# Idk what it does but its important
if __name__ == '__main__':
    while True:
        main()