import re

text = "hello_world_my_name_is_Aziza"
ans = re.findall(r"[a-z]_[a-z]",txt)
print(ans)
