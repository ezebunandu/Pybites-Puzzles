def _perm_sub_to_oct(perm_sub):
    result_string = "".join("0" if char == "-" else "1" for char in perm_sub)
    return int(result_string, 2)


def get_octal_from_file_permission(rwx: str) -> str:
    """Receive a Unix file permission and convert it to
    its octal representation.

    In Unix you have user, group and other permissions,
    each can have read (r), write (w), and execute (x)
    permissions expressed by r, w and x.

    Each has a number:
    r = 4
    w = 2
    x = 1

    So this leads to the following input/ outputs examples:
    rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
    rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
    r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
    """
    user_perm, group_perm, all_perm = rwx[:3], rwx[3:6], rwx[6:]
    user_oct, group_oct, all_oct = (
        _perm_sub_to_oct(user_perm),
        _perm_sub_to_oct(group_perm),
        _perm_sub_to_oct(all_perm),
    )
    return "".join([str(user_oct), str(group_oct), str(all_oct)])
