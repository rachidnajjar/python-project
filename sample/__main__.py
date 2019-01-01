import core
import datetime
from models import Personne
import youtube

def main():
    core.hmm()
    
    p = Personne("NAJJAR", "Amine", datetime.date(2008, 6, 14))
    age = p.obtenirAge(datetime.date(2010, 2, 15))
    print(age)
    
    youtubeScraper = youtube.Scraper()
    youtubeScraper.chercher("hassan+saleh")
    youtubeScraper.afficher()
    youtubeScraper.telecharger()


if __name__ == "__main__":
    main()