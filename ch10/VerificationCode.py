import random


def VerificationCode(length=6):
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    VerificationCodeString = ""
    for _ in range(length):
        VerificationCodeString += characters[random.randint(
            0,
            len(characters) - 1)]
    return VerificationCodeString