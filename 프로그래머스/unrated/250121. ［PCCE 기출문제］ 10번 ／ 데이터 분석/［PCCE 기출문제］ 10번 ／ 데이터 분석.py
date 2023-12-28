def solution(data, ext, val_ext, sort_by):
    contents = ["code", "date", "maximum", "remain"]
    return sorted(filter(lambda x:x[contents.index(ext)] < val_ext, data), key=lambda x:x[contents.index(sort_by)])