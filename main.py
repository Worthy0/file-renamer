from file_renamer import rename_files_in_directory, backup_directory

def main():
    directory = input("Klasörün tam yolunu girin: ").strip()
    replace_space_with = input("Boşlukları neyle değiştirmek istersiniz? ('_' ya da '-'): ").strip() or "_"
    case_preference = input("Dosya adlarını küçük harfe çevirmek ister misiniz? (e/h): ").lower() == 'e'

    # Yedekleme
    backup_path = backup_directory(directory)
    print(f"Yedekleme oluşturuldu: {backup_path}")

    # Yeniden adlandırma
    renamed_files, errors = rename_files_in_directory(directory, replace_space_with, case_preference)

    # Raporlama
    print("\nRapor:")
    print(f"Başarıyla yeniden adlandırılan dosyalar: {len(renamed_files)}")
    for old, new in renamed_files:
        print(f" - {old} -> {new}")

    if errors:
        print(f"\nHatalar: {len(errors)}")
        for filename, error in errors:
            print(f" - {filename}: {error}")

if __name__ == "__main__":
    main()
