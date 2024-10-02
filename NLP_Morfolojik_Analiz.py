def remove_affixes_turkish(word):
    # Türkçede yaygın ön ekler
    prefixes = ['en', 'en çok', 'en az']

    # Türkçede yaygın son ekler
    suffixes = ['ler', 'lar', 'ci', 'cı', 'lik', 'lık', 'da', 'de', 'ta', 'te', 'den', 'dan',
                'e', 'a', 'im', 'ım', 'sin', 'sın', 'siniz', 'sunuz', 'mız', 'miz', 'niz', 
                'nız', 'mızı', 'ımız', 'ınız', 'yiz', 'yız', 'lerim', 'larım', 'ım', 'im', 
                'um', 'üm', 'm', 'n', 'u', 'ü', 'yim', 'yım', 'yla', 'yla', 'deki', 'deki']

    for prefix in prefixes:
        if word.startswith(prefix):
            word = word[len(prefix):].strip()
            break  # İlk bulunan prefix çıkarılır

    
    for suffix in suffixes:
        if word.endswith(suffix):
            word = word[:-len(suffix)]
            break  # İlk bulunan suffix çıkarılır

    return word


def morphological_analysis(word):
    root = remove_affixes_turkish(word)
    if len(root) < 3:
        return word
    return root

#Örnekler
words = ['en küçük', 'kitaplar', 'ev','arabanız', 'okulda', 'çocukta', 'kedi', 'kalemim']

for word in words:
    root = morphological_analysis(word)
    print(f"Asıl kelime: {word} -> Kök: {root}")
