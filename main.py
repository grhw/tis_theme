import os
import generate


with open("theme/tis.big.css","w+") as f:
    f.write(f.read() + "\n" + "\n".join(generate.compiled))

compressed_css = os.system("csso ./theme/tis.big.css --output ./theme/tis.theme.css")