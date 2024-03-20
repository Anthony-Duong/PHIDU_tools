def test(arg):
    if arg not in ('yes', 'no'):
        raise TypeError()
    
    print('wow')
    
test('No')