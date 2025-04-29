import sys

def get_owner(file_path, codeowners_file='CODEOWNERS.txt'):
    try:
        with open(codeowners_file, 'r') as f:
            for line in f:
                # מתעלם משורות ריקות או שורות עם תו '#' (הערות)
                if line.strip() and not line.startswith('#'):
                    parts = line.split()
                    if parts:
                        # הנחה שהבעלים הוא הראשון בשורה
                        owner = parts[0]
                        # בדוק אם הנתיב נמצא בשורה
                        if file_path in parts[1:]:
                            return owner
        return "No owner found for this path."
    except FileNotFoundError:
        return f"File {codeowners_file} not found."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python parser.py <file_path>")
    else:
        file_path = sys.argv[1]
        owner = get_owner(file_path)
        print(f"The owner of '{file_path}' is: {owner}")
