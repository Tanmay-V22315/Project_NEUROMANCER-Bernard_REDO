def Txtpreprocessor(inputstring):
    if "<alias>" in inputstring:

        aliasdict = eval(inputstring[inputstring.index("<alias>")+len("<alias")+1:inputstring.index("</alias>")])

        inputstring = inputstring[inputstring.index("</alias>")+len("</alias>")+1:]

        for i in aliasdict.keys():
            inputstring = inputstring.replace(i,aliasdict[i])

        return Txtpreprocessor(inputstring)
    
    elif "<

    else:
        return inputstring




print(Txtpreprocessor("<alias>{'W3C':'World Wide Web Consortium', 'W3': 'World Wide Web', 'ISO': 'International standards organisation'}</alias> The W3C is the main ISO for the W3C. Founded in 1994 and currently led by Tim Berners-Lee, the consortium is made up of member organizations that maintain full-time staff working together in the development of standards for the W3."))