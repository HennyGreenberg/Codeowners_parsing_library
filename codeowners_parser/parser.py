import sys
import os
import fnmatch

def get_owner(file_path, codeowners_file='.github/CODEOWNERS.txt'):
    try:
        with open(codeowners_file, 'r') as f:
            owners = []
            for line in f:
                # מתעלם משורות ריקות או שורות עם תו '#' (הערות)
                if line.strip() and not line.startswith('#'):
                    parts = line.split()
                    if len(parts) >= 2:
                        # הבעלים הוא האחרון בשורה
                        owner = parts[-1]
                        # דפוסים הם כל מה שקדום לבעלים
                        patterns = parts[:-1]

                        # בדוק אם הנתיב תואם לאחד מהדפוסים
                        for pattern in patterns:
                            if fnmatch.fnmatch(file_path, pattern):
                                owners.append(owner)

            # אם יש בעלים, החזר את האחרון ברשימה
            if owners:
                return owners[-1]
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
