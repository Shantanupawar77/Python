DICT={
    "pankha":"fan",
    "dabba":"box",
    "vastu":"item"
}
print("Options are ",DICT.keys())
a=input("Enter the hindi word:\n")
print("The meaning of your word is ",DICT[a])
print("The meaning of your word is ",DICT.get(a))