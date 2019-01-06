import random

while True:
    print()
    print("Welcome to Bruce's Fortune Telling Program")
    print()
    name = input("Please enter your name to have your fortune told to you: ",)
    print()

    # Dictionary used for my data structure to hold the fortunes
    fortunes = {1:"A beautiful, smart, and loving person will be coming into your life.", 2:"A lifetime friend shall soon be made.",
    3:"A pleasant surprise is waiting for you.", 4:"All the effort you are making will ultimately pay off.",
    5:"All the troubles you have will pass away very quickly.", 6:"All will go well with your new project.", 7:"All your hard work will soon pay off.", 
    8:"Don’t worry; prosperity will knock on your door soon.", 9:"An important person will offer you support.", 10:"Good news will come to you by mail.",
    11:"New people will bring you new realizations, especially about big issues.", 12:"Riches from heaven find their way to your doorstep this year!",
    13:"Romance moves you in a new direction.", 14:"Someone you care about seeks reconciliation.", 15:"You will always be surrounded by true friends.",
    16:"You will always get what you want through your charm and personality.", 17:"You will always have good luck in your personal affairs.",
    18:"You will be a great success both in the business world and society.", 19:"You will be blessed with a long life.", 20:"You will be pleasantly surprised tonight.",
    21:"You will be sharing great news with all the people you love.", 22:"You will be successful in your work.", 23:"You will be traveling and coming into a fortune.",
    24:"You will be unusually successful in business.", 25:"You will become a great philanthropist in your later years.", 26:"You will become incredibly wealthy",
    27:"You will enjoy good health.", 28:"You will be surrounded by luxury.", 29:"You will inherit a large sum of money.", 30:"You will soon be surrounded by good friends and laughter.",
    31:"You will travel far and wide for both business and pleasure.", 32:"Your ability to juggle many tasks will take you far.", 33:"Your difficulties will strengthen you.",
    34:"Your energy will return and you will get things done.", 35:"Your hard work will payoff today.", 36:"Your ideals are well within your reach. All you have to do is try for them.",
    37:"Your infinite capacity for patience will be rewarded sooner or later.", 38:"Your leadership qualities will be tested and proven.", 
    39:"Your life will be happy and peaceful.", 40:"Your life will become more exciting.", 41:"Your love life will be happy and harmonious.", 
    42:"Your passion will be an important part of your life.", 43:"Your quick wits will get you out of a tough situation.", 44:"Your success will astonish everyone.",
    45:"Your talents will be recognized and suitably rewarded.", 46:"Your work interests will capture the highest status or prestige.", 
    47:"A thrilling time is in your immediate future.", 48:"Plan for many pleasures ahead.", 49:"Something you lost will soon turn up.", 
    50:"Your many hidden talents will become obvious to those around you.", 51:"You will be hanged for drug smuggling in Thailand.", 
    52:"You will change your mind and end up shunned by your friends and family.", 53:"Good luck fucker, you are going to need it.", 
    54:"You will be sucking dirt soon whether you want to or not.", 55:"The FBI will soon arrest you for all of the pornography you have been looking at.", 
    56:"You will soon go on a killing spree that will make you infamous.", 57:"Your friends and family will conspire to remove you from the earth.",
    58:"North Korea will nuke you.", 59:"A gamma ray burst will kill all life on earth including you.", 60:"The police will claim they killed you in self-defense.",
    61:"You're not being paranoid, everyone is out to get you.", 62:"You will be diagnosed as an incurable a-hole.", 63:"Fatal heart attack in 5,4,3,2,1",
    64:"That upcoming knife fight that you are going to be in is not going to end well for you.", 65:"You will end up in the morgue soon.", 
    66:"You will have a horrible case of diarrhea in front of everyone at work.", 67:"The TSA will find the drugs you hid after the cavity search.", 
    68:"Somehow you will end up being banned from the Internet for life.", 69:"You will die broke and alone in a trailer park.", 
    70:"You will be swindled out of all your money within the year.", 71:"Are you broke yet? If not, you will be soon.",
    72:"You will be savagely killed in N Africa by Islamic terrorists and everyone at your high school reunion will laugh about it.", 
    73:"Everyone will lose all faith in your abilities.", 74:"Your significant other will cheat on you with everyone they meet.", 
    75:"You will be transported to an alternate universe where everyone takes turns abusing you.", 76:"You will never die even though you will continue to age.", 
    76:"Your symptoms are just omens of your impending doom.", 77:"There is no god, but there is a hell and you are going to spend eternity there soon.", 
    78:"This is just the beginning of the end for you.", 79:"Nobody will ever love you again after the horrible car accident.", 
    80:"Hahaha, trust me. You don't want to know what is going to happen to you.", 81:"Good friends are rare, especially for you as you will never have any.",
    82:"Your upcoming adventures as a prostitute will not be as lucrative as you hope.", 83:"You will sell your soul to Lucifer in exchange for a failed marriage.",
    84:"Your gut instincts are right. You are running out of time.", 85:"You will join ISIS as a desperate means for attention.",
    86:"Your death will be one of the most watched videos ever on YouTube.", 87:"Once you realize what is happening, it will be too late to save yourself.",
    88:"All of your hopes and dreams will be permanently sidelined when you start your career in porn.", 89:"Do you like caskets? Because soon you will be in one.",
    90:"You won't be able to hide your heroin addiction.", 91:"The government is going to make an example out of you.", 
    92:"The heroin epidemic will not spare you.", 93:"You will be remembered as the canary in the coalmine of the upcoming pandemic.", 
    94:"You will become more spiritually aware when you join a death cult.", 95:"Your sex tape will make you the talk of the town.", 
    96:"Enjoy your freedom, it won't last much longer.", 97:"When you finally snap, nobody will be able to stop you from making a fool out of yourself.", 
    98:"The voices in your head will just be the beginning of your long downward slide into madness.", 99:"Your career as a scientist will be shortlived thanks to your low IQ.",
    100:"You will be shocked at all of the abuse you will have to endure during your remaining years."}

    yourFortune = random.randint(0,100) # Random integer range picks a random fortune for the user. 

    print(name, "- Here is your Fortune!! - ",fortunes[yourFortune])
    print()

    while True:
        answer = input('Run again? (y/n): ')
        if answer in ('y', 'n'):
            break
        print('Invalid input.')
    if answer == 'y':
        continue
    else:
        print('Goodbye')
        break
