print("n Main Function Demo n")


def demo(got):
    print("&amp;hellip;Beginning Game Of Thrones&amp;hellip;n")
    new_got = str.split(got)
    print("&amp;hellip;Game of Thrones has finished&amp;hellip;n")
    return new_got


def main():
    got = "n Bran Stark wins the Iron Throne n"
    print(got)
    new_got = demo(got)
    print(new_got)


if __name__ == "__main__":
    main()
