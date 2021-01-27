from fastapi import FastAPI


app = FastAPI()

def is_palindrome( input_data ):

    input_data =  str(input_data)
    i = 0
    l = len(input_data)-1

    while i < l:
        if input_data[i] != input_data[l]:
            return False
        i+=1
        l-=1

    return True


@app.get("/ispalindrome/{input_data}")
def is_input_a_palindrome(input_data: str):

    return is_palindrome(input_data)

