def iter_by_punctuations(paragraph):
    head = 0
    tail = head
    while head < len(paragraph):
        while tail < len(paragraph):
            tail += 1
            if tail >= len(paragraph):
                yield paragraph[head : tail + 1]
                head = tail + 1
                tail = head
                break
            if paragraph[tail] in "!,.:;?":
                yield paragraph[head : tail + 1]
                head = tail + 1
                tail = head


def iter_by_space(paragraph):
    for item in paragraph.split():
        yield item


def iter_no_split(paragraph):
    yield paragraph
