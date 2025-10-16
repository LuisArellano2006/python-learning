# hw3_Arellano_Luis.py
# Luis Arellano
# 2025-09-14

import re

def format_receipt(items, prices, quantities):
    if len(items) != len(prices) or len(items) != len(quantities):
        return "Error: Input lists must have the same length"
    
    receipt = "=" * 28 + "\n"
    receipt += f"{'Item':<20}{'Qty':^5}{'Price':>8}\n"
    receipt += "=" * 28 + "\n"
    
    total = 0
    for i in range(len(items)):
        item_total = prices[i] * quantities[i]
        total += item_total
        receipt += f"{items[i]:<20}{quantities[i]:^5}$ {item_total:>7.2f}\n"
    
    receipt += "=" * 28 + "\n"
    receipt += f"{'TOTAL':<26}$ {total:>7.2f}\n"
    receipt += "=" * 28
    
    return receipt

def process_user_data(raw_data):
    cleaned = {}
    
    name = raw_data.get('name', '').strip().title()
    cleaned['name'] = name
    
    email = raw_data.get('email', '').strip().lower().replace(' ', '')
    cleaned['email'] = email
    
    phone = raw_data.get('phone', '')
    phone_clean = ''.join(char for char in phone if char.isdigit())
    cleaned['phone'] = phone_clean
    
    address = raw_data.get('address', '').strip().title()
    address_clean = ' '.join(address.split())
    cleaned['address'] = address_clean
    
    name_parts = name.split()
    if len(name_parts) >= 2:
        username = f"{name_parts[0].lower()}_{name_parts[1].lower()}"
    else:
        username = name.lower().replace(' ', '_')
    cleaned['username'] = username
    
    validation = {
        'name_valid': len(name) > 0,
        'email_valid': '@' in email and '.' in email,
        'phone_valid': len(phone_clean) == 10 or len(phone_clean) == 11,
        'address_valid': len(address_clean) > 0
    }
    cleaned['validation'] = validation
    
    return cleaned

def analyze_text(text):
    if not text:
        return {
            'total_chars': 0, 'total_words': 0, 'total_lines': 0,
            'avg_word_length': 0, 'most_common_word': '', 'longest_line': '',
            'words_per_line': [], 'capitalized_sentences': 0,
            'questions': 0, 'exclamations': 0
        }
    
    lines = text.split('\n')
    words = text.split()
    
    total_chars = len(text)
    total_words = len(words)
    total_lines = len(lines)
    
    if total_words > 0:
        avg_word_length = round(sum(len(word) for word in words) / total_words, 2)
    else:
        avg_word_length = 0
    
    word_count = {}
    for word in words:
        clean_word = word.strip('.,!?;:').lower()
        if clean_word:
            word_count[clean_word] = word_count.get(clean_word, 0) + 1
    
    if word_count:
        most_common_word = max(word_count.items(), key=lambda x: x[1])[0]
    else:
        most_common_word = ''
    
    longest_line = max(lines, key=len, default='')
    
    words_per_line = [len(line.split()) for line in lines]
    
    sentences = re.split(r'[.!?]', text)
    capitalized_sentences = 0
    questions = text.count('?')
    exclamations = text.count('!')
    
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and sentence[0].isupper():
            capitalized_sentences += 1
    
    return {
        'total_chars': total_chars,
        'total_words': total_words,
        'total_lines': total_lines,
        'avg_word_length': avg_word_length,
        'most_common_word': most_common_word,
        'longest_line': longest_line,
        'words_per_line': words_per_line,
        'capitalized_sentences': capitalized_sentences,
        'questions': questions,
        'exclamations': exclamations
    }

def find_patterns(text):
    patterns = {
        'integers': r'\b\d+\b',
        'decimals': r'\b\d+\.\d+\b',
        'words_with_digits': r'\b\w*\d\w*\b',
        'capitalized_words': r'\b[A-Z][a-z]*\b',
        'all_caps_words': r'\b[A-Z]{2,}\b',
        'repeated_chars': r'\b\w*(\w)\1\w*\b'
    }
    
    results = {}
    for key, pattern in patterns.items():
        if key == 'repeated_chars':
            word_pattern = r'\b\w*(\w)\1\w*\b'
            words_with_repeats = []
            for match in re.finditer(word_pattern, text):
                words_with_repeats.append(match.group())
            results[key] = words_with_repeats
        else:
            matches = re.findall(pattern, text)
            results[key] = matches
    
    return results

def validate_format(input_string, format_type):
    patterns = {
        'phone': r'^\((\d{3})\)\s*(\d{3})-(\d{4})$|^(\d{3})-(\d{3})-(\d{4})$',
        'date': r'^(0[1-9]|1[0-2])/(0[1-9]|[12]\d|3[01])/(\d{4})$',
        'time': r'^([01]?\d|2[0-3]):([0-5]\d)\s*([AP]M)?$|^([01]?\d):([0-5]\d)\s*([ap]m)$',
        'email': r'^(\w+[.\w]*)@(\w+[-\w]*)\.([a-zA-Z]{2,})$',
        'url': r'^https?://([\w-]+\.)+[\w-]+(/[\w-./?%&=]*)?$',
        'ssn': r'^(\d{3})-(\d{2})-(\d{4})$'
    }
    
    pattern = patterns.get(format_type)
    if not pattern:
        return False, None
    
    match = re.match(pattern, input_string.strip())
    
    if not match:
        return False, None
    
    extracted_parts = {}
    
    if format_type == 'phone':
        groups = match.groups()
        if groups[0]:
            extracted_parts = {'area_code': groups[0], 'prefix': groups[1], 'line': groups[2]}
        else:
            extracted_parts = {'area_code': groups[3], 'prefix': groups[4], 'line': groups[5]}
    
    elif format_type == 'date':
        extracted_parts = {'month': match.group(1), 'day': match.group(2), 'year': match.group(3)}
    
    elif format_type == 'time':
        groups = match.groups()
        if groups[2]:
            extracted_parts = {'hour': groups[0], 'minute': groups[1], 'period': groups[2]}
        else:
            extracted_parts = {'hour': groups[3] or groups[0], 'minute': groups[4] or groups[1]}
    
    elif format_type == 'email':
        extracted_parts = {'username': match.group(1), 'domain': match.group(2), 'extension': match.group(3)}
    
    elif format_type == 'url':
        extracted_parts = {'domain': match.group(1), 'path': match.group(2) or ''}
    
    elif format_type == 'ssn':
        extracted_parts = {'first_three': match.group(1), 'middle_two': match.group(2), 'last_four': match.group(3)}
    
    return True, extracted_parts

def extract_information(text):
    results = {}
    
    price_pattern = r'\$\d{1,3}(?:,\d{3})*\.\d{2}|\$\d+\.\d{2}'
    results['prices'] = re.findall(price_pattern, text)
    
    percentage_pattern = r'\b\d+(?:\.\d+)?%'
    results['percentages'] = re.findall(percentage_pattern, text)
    
    year_pattern = r'\b(19|20)\d{2}\b'
    results['years'] = re.findall(year_pattern, text)
    
    sentence_pattern = r'[^.!?]*[.!?]'
    sentences = re.findall(sentence_pattern, text)
    results['sentences'] = [s.strip() for s in sentences if s.strip()]
    
    question_pattern = r'[^.?]*\?'
    questions = re.findall(question_pattern, text)
    results['questions'] = [q.strip() for q in questions if q.strip()]
    
    quote_pattern = r'"([^"]*)"'
    results['quoted_text'] = re.findall(quote_pattern, text)
    
    return results

def clean_text_pipeline(text, operations):
    if not text:
        return {'original': text, 'cleaned': text, 'steps': []}
    
    current_text = text
    steps = [current_text]
    
    for operation in operations:
        if operation == 'trim':
            current_text = current_text.strip()
        elif operation == 'lowercase':
            current_text = current_text.lower()
        elif operation == 'remove_punctuation':
            current_text = re.sub(r'[^\w\s]', '', current_text)
        elif operation == 'remove_digits':
            current_text = re.sub(r'\d', '', current_text)
        elif operation == 'remove_extra_spaces':
            current_text = re.sub(r'\s+', ' ', current_text).strip()
        elif operation == 'remove_urls':
            current_text = re.sub(r'https?://\S+', '', current_text)
        elif operation == 'remove_emails':
            current_text = re.sub(r'\S+@\S+\.\S+', '', current_text)
        elif operation == 'capitalize_sentences':
            sentences = re.split(r'([.!?] )', current_text)
            current_text = ''
            for i in range(0, len(sentences), 2):
                if i < len(sentences):
                    sentence = sentences[i]
                    if sentence:
                        current_text += sentence[0].upper() + sentence[1:]
                    if i + 1 < len(sentences):
                        current_text += sentences[i + 1]
        
        steps.append(current_text)
    
    return {
        'original': text,
        'cleaned': current_text,
        'steps': steps
    }

def smart_replace(text, replacements):
    if not text:
        return text
    
    result = text
    
    contractions = {
        "don't": "do not", "won't": "will not", "can't": "cannot",
        "I'm": "I am", "You're": "you are", "It's": "it is",
        "he's": "he is", "she's": "she is", "We're": "we are",
        "they're": "they are", "I've": "I have", "You've": "you have",
        "We've": "we have", "they've": "they have"
    }
    
    number_words = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    
    if replacements.get('censor_phone'):
        phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
        result = re.sub(phone_pattern, 'XXX-XXX-XXXX', result)
    
    if replacements.get('censor_email'):
        email_pattern = r'\S+@\S+\.\S+'
        result = re.sub(email_pattern, '[EMAIL]', result)
    
    if replacements.get('fix_spacing'):
        result = re.sub(r'\s+([.,!?;:])', r'\1', result)
        result = re.sub(r'([.,!?;:])(\w)', r'\1 \2', result)
    
    if replacements.get('expand_contractions'):
        for contraction, expansion in contractions.items():
            result = result.replace(contraction, expansion)
    
    if replacements.get('number_to_word'):
        for digit, word in number_words.items():
            result = re.sub(r'\b' + digit + r'\b', word, result)
    
    return result

def analyze_log_file(log_text):
    if not log_text:
        return {
            'total_entries': 0, 'error_count': 0, 'warning_count': 0,
            'info_count': 0, 'dates': [], 'error_messages': [],
            'time_range': ('', ''), 'most_active_hour': 0
        }
    
    lines = log_text.strip().split('\n')
    log_pattern = r'\[(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})\] (\w+): (.*)'
    
    entries = []
    error_count = 0
    warning_count = 0
    info_count = 0
    dates = set()
    error_messages = []
    times = []
    hour_counts = {}
    
    for line in lines:
        match = re.match(log_pattern, line.strip())
        if match:
            date, time, level, message = match.groups()
            entries.append({
                'date': date, 'time': time, 'level': level, 'message': message
            })
            
            dates.add(date)
            times.append(time)
            
            if level.upper() == 'ERROR':
                error_count += 1
                error_messages.append(message)
            elif level.upper() == 'WARNING':
                warning_count += 1
            elif level.upper() == 'INFO':
                info_count += 1
            
            hour = int(time.split(':')[0])
            hour_counts[hour] = hour_counts.get(hour, 0) + 1
    
    if times:
        time_range = (min(times), max(times))
    else:
        time_range = ('', '')
    
    if hour_counts:
        most_active_hour = max(hour_counts.items(), key=lambda x: x[1])[0]
    else:
        most_active_hour = 0
    
    return {
        'total_entries': len(entries),
        'error_count': error_count,
        'warning_count': warning_count,
        'info_count': info_count,
        'dates': sorted(list(dates)),
        'error_messages': error_messages,
        'time_range': time_range,
        'most_active_hour': most_active_hour
    }

def run_tests():
    print("="*50)
    print("Testing Part 1: String Methods")
    print("="*50)
    
    items = ["Coffee", "Sandwich"]
    prices = [3.50, 8.99]
    quantities = [2, 1]
    receipt = format_receipt(items, prices, quantities)
    print("Receipt Test:")
    print(receipt)
    
    test_data = {
        'name': ' john DOE ',
        'email': ' JOHN@EXAMPLE.COM ',
        'phone': '(555) 123-4567',
        'address': '123 main street'
    }
    cleaned = process_user_data(test_data)
    print(f"\nCleaned name: {cleaned.get('name', 'ERROR')}")
    print(f"Cleaned email: {cleaned.get('email', 'ERROR')}")
    
    print("\n" + "="*50)
    print("Testing Part 2: Regular Expressions")
    print("="*50)
    
    test_text = "I have 25 apples and 3.14 pies"
    patterns = find_patterns(test_text)
    print(f"Found integers: {patterns.get('integers', [])}")
    print(f"Found decimals: {patterns.get('decimals', [])}")
    
    phone_valid, phone_parts = validate_format("(555) 123-4567", "phone")
    print(f"\nPhone validation: {phone_valid}")
    if phone_parts:
        print(f"Extracted parts: {phone_parts}")
    
    info_text = 'The price is $19.99 (20% off).'
    info = extract_information(info_text)
    print(f"\nPrices found: {info.get('prices', [])}")
    print(f"Percentages found: {info.get('percentages', [])}")
    
    print("\n" + "="*50)
    print("Testing Part 3: Combined Operations")
    print("="*50)
    
    dirty_text = " Hello WORLD! "
    operations = ['trim', 'lowercase', 'remove_extra_spaces']
    cleaned_result = clean_text_pipeline(dirty_text, operations)
    print(f"Original: '{cleaned_result.get('original', '')}'")
    print(f"Cleaned: '{cleaned_result.get('cleaned', '')}'")
    
    print("\n" + "="*50)
    print("Testing Part 4: Log Analysis")
    print("="*50)
    
    sample_log = """[2024-01-15 10:30:45] ERROR: Connection failed
[2024-01-15 10:31:00] INFO: Retry attempt
[2024-01-15 10:32:00] WARNING: Timeout warning"""
    
    log_analysis = analyze_log_file(sample_log)
    print(f"Total entries: {log_analysis.get('total_entries', 0)}")
    print(f"Error count: {log_analysis.get('error_count', 0)}")
    print(f"Unique dates: {log_analysis.get('dates', [])}")
    
    print("\n" + "="*50)
    print("All tests completed!")
    print("="*50)

if __name__ == "__main__":
    run_tests()