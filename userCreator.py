import argparse
import sys
import os
import time
nombre=''
apellido=''
nombres=[]
apellidos=[]
def combinacionNombre(m,n):
    newUser.append(m+n)
    newUser.append(m+'.'+n)
    newUser.append(m+'_'+n)
    newUser.append(m+'-'+n)
def create_arg_parser():
    # Creates and returns the ArgumentParser object.

    parser = argparse.ArgumentParser(description='Description of your app.')
    parser.add_argument('-u',
                    help='User FIle')
    parser.add_argument('-o',
                    help='Output file with user variations')
    parser.add_argument('-one',
                    help='just 1 user')
    parser.add_argument('-mix',
                    help='User FIle')
    return parser


if __name__ == "__main__":
    users=[]
    newUser=[]
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    if parsed_args.one != None:
        nombre=parsed_args.one[:parsed_args.one.find(' ')].lower()
        apellido=parsed_args.one[parsed_args.one.find(' ')+1:].lower()
        k=len(nombre)
        kk=len(apellido)
        for p in range(k):
            for pp in range(kk):
                combinacionNombre(nombre[0:p+1],apellido[0:pp+1])
        for p in range(kk):
            for pp in range(k):
                combinacionNombre(apellido[0:p+1],nombre[0:pp+1])
        for g in newUser:
            print(g)
    elif parsed_args.u != None and os.path.exists(parsed_args.u) and parsed_args.one == None and parsed_args.mix == None:
        print("File exist:" + parsed_args.u)
        r = open(parsed_args.u, "r")
        count1 = 0
        for t in r:
            count1 += 1
        r.close()
        r = open(parsed_args.u, "r")
        count=0
        for x in r:
            count +=1
            nombre=x[:x.find(' ')].lower()
            apellido=x[x.find(' ')+1:].lower()
            users.append(x)
            newUser.append(x)
            # newUser.append(x.replace(' ','.'))
            # newUser.append(x.replace(' ',''))
            # newUser.append(x.replace(' ','_'))
            # newUser.append(x.replace(' ','-'))
            # Con nombre
            k=len(nombre)
            kk=len(apellido)
            if count << count1:
                for p in range(k):
                    for pp in range(kk):
                        combinacionNombre(nombre[0:p+1],apellido[0:pp])
                for p in range(kk):
                    for pp in range(k):
                        combinacionNombre(apellido[0:p],nombre[0:pp+1])
            else:
                for p in range(k):
                    for pp in range(kk):
                        combinacionNombre(nombre[0:p+1],apellido[0:pp+1])
                for p in range(kk):
                    for pp in range(k):
                        combinacionNombre(apellido[0:p+1],nombre[0:pp+1])
        r.close()
        print(len(users))     
        for l in newUser:
            if len(l)>=2:
                print(l)
        print(len(users))
    elif parsed_args.mix != None and parsed_args.u != None and os.path.exists(parsed_args.u):
        r = open(parsed_args.u, "r")
        count1 = 0
        for t in r:
            count1 += 1
            nombres.append(t[:t.find(' ')].lower())
            apellidos.append(t[t.find(' ')+1:].lower())
        r.close()
        r = open(parsed_args.u, "r")
        for x in range(len(nombres)):
            count = 0
            nombre=nombres[x]
            for xx in range(len(apellidos)):
                count += 1
                apellido=apellidos[xx]
                k=len(nombre)
                kk=len(apellido)
                if count << count1:
                    for p in range(k):
                        for pp in range(kk):
                            combinacionNombre(nombre[0:p+1],apellido[0:pp])
                    for p in range(kk):
                        for pp in range(k):
                            combinacionNombre(apellido[0:p],nombre[0:pp+1])
                else:
                    for p in range(k):
                        for pp in range(kk):
                            combinacionNombre(nombre[0:p+1],apellido[0:pp+1])
                    for p in range(kk):
                        for pp in range(k):
                            combinacionNombre(apellido[0:p+1],nombre[0:pp+1])
    print(len(newUser))
    print(parsed_args.o)
    r = open(parsed_args.o, "a")
    for x in newUser:
        r.write(x+'\n')
    r.close()
            
       
       
       
       