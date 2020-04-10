# My-ROPemporium-Solutions
My solutions to ROPemporium return-oriented programming challenges.

https://ropemporium.com/

ROPing is necessary to bypass mitigations such as ASLR, W^X,...

It allows you to abuse bytes already present in the binary thus using the binary against itself.

Tools:
- ROPgadget: https://github.com/JonathanSalwan/ROPgadget
- Ropper: https://github.com/sashs/Ropper
- readelf
- objdump
- GDB with PEDA: https://github.com/longld/peda

I should also mention pwntools: https://github.com/Gallopsled/pwntools which is a must when participating in CTFs. (I didn't use it here)

Advice:
Tools like ROPgadget can generate ROP chains for you, but I think doing it manually is very important to get a grasp on how to choose and chain gadgets correctly.

