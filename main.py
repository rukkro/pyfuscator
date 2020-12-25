import sys, inspect

MAX_CHR = 25565
OBFUSCATOR_FUNC = "lambda v: '|' + (v*'_') + '|'"
SPLIT_VAR = "8/8"
VAR_MAPPER_FUNC = f"""[setattr(sys.modules[__name__], ({OBFUSCATOR_FUNC})(v), chr(v)) for v in range({MAX_CHR}) if (sys:=__import__('sys'))]"""

# Global variable Mapper
exec(VAR_MAPPER_FUNC)

# The code import
input_file = __import__('tst')
lines: str = inspect.getsource(input_file)

# Encoder
encoded_file =[
    eval(f"({OBFUSCATOR_FUNC})({ord(i)})", globals()) for i in lines
]
print(encoded_file)

with open('tst.py','w',encoding='utf-8') as tstfile:
    pre = "# coding=utf8\n"
    encoded_with_decoder = f""""".join(getattr(sys.modules[__name__], i) for i in {encoded_file})"""
    code = f"""{VAR_MAPPER_FUNC} and exec({encoded_with_decoder},globals())"""
    tstfile.write(pre)
    tstfile.write(code)



with open('tst.py','r',encoding='utf-8') as importfileed:

    # Decoder
    bb = "".join([
        getattr(sys.modules[__name__], i) for i in importfileed.read()
    ])
    # Executor
    exec(bb)
hello = '''abc'''
