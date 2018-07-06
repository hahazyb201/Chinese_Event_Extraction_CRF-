'''
*****************
This file is not useful. Don't use this
*****************
'''
with open("./Testfile",'r',encoding='UTF-8') as ft:
    with open("./CharacterTestFile",'w',encoding='UTF-8') as fc:
        word_items=ft.readlines()
        for line in word_items:
            wordLabel=line.split()
            print(wordLabel)
            if len(wordLabel)==0:
                fc.write("\n")
                continue
            word=wordLabel[0]
            if len(wordLabel)==1:
            	continue
            for i in range(len(word)):
                if wordLabel[1][0]=='B':
                    if i==0:
                        fc.write(word[i]+"\t"+wordLabel[1]+"\n")
                    else:
                        fc.write(word[i]+"\t"+"I"+wordLabel[1][1:]+"\n")
                else:
                    fc.write(word[i]+"\t"+wordLabel[1]+"\n")
