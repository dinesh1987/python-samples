#PF-Assgn-30
def encode(message):
    dup_count=0
    encoded_message=""
    len_message=len(message)
    for loopCnt in range(0,len_message):
        if(loopCnt+1!=len_message and message[loopCnt]==message[loopCnt+1]):
            dup_count+=1
        else:
            if(dup_count>0):
                encoded_message=encoded_message+str(dup_count+1)+message[loopCnt]
            else:
                encoded_message=encoded_message+message[loopCnt]
            dup_count=0
    return encoded_message
    #Remove pass and write your logic here

#Provide different values for message and test your program
print("Encoded Message:",encode("ABBBBCCCCCCCCBB"))