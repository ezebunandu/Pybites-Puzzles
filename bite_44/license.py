import string
import secrets


def gen_key(parts=4, chars_per_part=8):
    """
    Generates a license key with the format: KI80OMZ7-5OGYC1AC-735LDPT1-4L11XU1U

    The key consist of a combination of upper case letters and digits

    parts: the number of parts in the license key
    chars_per_part: number of characters per part
    """
    alphabet = string.ascii_letters.upper() + string.digits
    partials = [
        "".join(secrets.choice(alphabet) for i in range(chars_per_part))
        for _ in range(parts)
    ]
    return "-".join(partials)


if __name__ == "__main__":
    print(gen_key())
