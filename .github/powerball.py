import pandas as pd

def load_data(file_path):
    """
    Load lottery data from a CSV file.
    Assumes two columns: 'draw_number' and 'numbers'.
    'numbers' are expected to be space-separated.
    """
    data = pd.read_csv(file_path)
    data['numbers'] = data['numbers'].apply(lambda x: [int(num) for num in x.split()])
    return data

def calculate_weighted_frequencies(data, decay_rate=0.9):
    """
    Calculate weighted frequencies of lottery numbers.
    More recent draws are given higher weights.
    """
    max_draw_number = data['draw_number'].max()
    frequencies = {}

    for _, row in data.iterrows():
        draw_age = max_draw_number - row['draw_number']
        weight = decay_rate ** draw_age
        for number in row['numbers']:
            frequencies[number] = frequencies.get(number, 0) + weight

    return frequencies

def normalize_probabilities(frequencies):
    """
    Convert frequencies to probabilities by normalizing.
    """
    total_weight = sum(frequencies.values())
    probabilities = {num: freq / total_weight for num, freq in frequencies.items()}
    return probabilities

def main():
    file_path = 'lottery_data.csv'  # Replace with your actual file path
    decay_rate = 0.95  # Adjust this value as needed

    data = load_data(file_path)
    frequencies = calculate_weighted_frequencies(data, decay_rate)
    probabilities = normalize_probabilities(frequencies)

    sorted_probabilities = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)

    print("Lottery Number Probabilities:")
    for number, probability in sorted_probabilities:
        print(f"Number {number}: {probability:.4f}")

if __name__ == "__main__":
    main()
