import random

def game():
    random_number = random.randint(0, 100)
    print("Selamat datang di Game Tebak Angka!")
    print("==========================================================================================")
    print("ANDA AKAN MEMILIKI KESEMPATAN UNTUK MENEBAK ANGKA YANG TELAH SAYA SIMPAN ! SEMOGA BERHASIL")

    while True:
        attempt = input("Masukkan berapa kesempatan yang anda miliki: ")
        if not attempt.isdigit() or int(attempt) < 1:
            print("Input tidak valid, harap masukkan angka positif.")
            continue
        attempts_left = int(attempt)

        while attempts_left > 0:
            guess = input("Tebak angka dari 0 hingga 100: ")
            if not guess.isdigit() or int(guess) < 0 or int(guess) > 100:
                print("Input tidak valid, harap masukkan angka dari 0 hingga 100.")
                continue

            guessed_number = int(guess)

            if guessed_number == random_number:
                print("Selamat! Angka yang Anda tebak adalah benar.")
                print ("C O N G R A T U L A T I O N !! ")
                break
            else:
                if guessed_number < random_number:
                    print("SALAH !!!!!!!, Tebakkanmu terlalu kecil")
                else:
                    print("SALAH !!!!!!!, Tebakkanmu terlalu besar")
                attempts_left -= 1

        if attempts_left == 0:
            print(f"GAME OVER !! YOU LOSE, NICE TRY !! Angka yang benar adalah {random_number}.")

        while True:
            play_again = input("Anda ingin bermain lagi? (Y/N): ").lower()
            if play_again == "y":
                return True
            elif play_again == "n":
                return False
            else:
                print("Input tidak valid, harap masukkan 'Y' atau 'N'.")
                continue
            
while game():
    pass

print("Terima kasih telah bermain Game Tebak Angka!")
