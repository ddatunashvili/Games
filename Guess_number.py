def main():
    print("-----------------------------------------------------")
    import random
    rnd = random.randint(0, 99)
    qula=5
    cda=1
    answer=input(" *^_^* ginda tamashis dawyeba? (ki/ara)").lower().strip()
    print("-----------------------------------------------------")
    if answer.lower().strip() == "ki":
        # ერთერთი ვარიაცია დაწერეს იმუშავებს
        print("Dasawyisistvis gaqvs", qula,'qula')
        print("-----------------------------------------------------")

        while True :
            #შეგყავს რიცხვი
            number = input("Chawere savaraudo ricxvi (0/100) ")
            print("-----------------------------------------------------")
            # დეფოლტზე აყენია შეყვანაზე რომ არის  სტრინგი (" ")
            number = int(number)
            if number > rnd :
                print("dabali ricxvi")
                print("-----------------------------------------------------")

                qula=qula-1
                cda=cda+1
                print("gagixda", qula,"qula")
                print("-----------------------------------------------------")

            else :
                if number < rnd :
                    print("magali ricxvi")
                    print("-----------------------------------------------------")
                    qula=qula-1
                    cda=cda+1
                    print("gagixda", qula,"qula")
                    print("-----------------------------------------------------")
                else:
                    print("yochag shen gamoicani chafiqrebuli ricxvi")
                    print("-----------------------------------------------------")
                    print("shen gaqvs",100/cda,"% gamocnobis unari")
                    print("-----------------------------------------------------")
                    if cda<5:
                        print("vau geniosixar ", cda,"cdashi gamoicani =^_^= =^_^=")
                        print("-----------------------------------------------------")
                        answer=input("ginda tamashis gagrdzeleba? (ki/ara)").lower().strip()
                        print("-----------------------------------------------------")
                        if answer.lower().strip() == "ki":
                            main()
                        else:
                            print("shen ar ginda datunias unda (^_^)")
                            print("-----------------------------------------------------")
                    else:
                        print("didi araferi",cda,"cdashi gamoicani")
                        answer=input("ginda tamashis gagrdzeleba? (ki/ara)").lower().strip()
                        print("-----------------------------------------------------")
                        if answer.lower().strip() == "ki":
                            main()
                        else:
                            print("shenc ar myavde nichieri.. (>_<)")
                            print("-----------------------------------------------------")
                            break
    else:
        print("aba raginda adamiano.... >_< >_<  ?!")
        print("-----------------------------------------------------")

main()
