import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))