import random
import shutil
from pathlib import Path

SRC = Path(r"C:\Users\Woori\Desktop\wori\261016_4_classificaitonmodel")
DST = SRC / "dataset"
CLASSES = ["happy", "normal", "sad"]
N_TRAIN, N_VAL, N_TEST = 70, 15, 15
SEED = 42


def split_class(cls):
    files = sorted(p for p in (SRC / cls).iterdir() if p.is_file())

    #   1) SEED 로 시드를 고정한 뒤 files 를 무작위로 섞기
    random.seed(SEED)
    random.shuffle(files)
    
    #   2) N_TRAIN / N_VAL / N_TEST 개수대로 슬라이싱 -> train_files, val_files, test_files
    train_files = files[:N_TRAIN]
    val_files = files[N_TRAIN:N_TRAIN + N_VAL]
    test_files = files[N_TRAIN + N_VAL:N_TRAIN + N_VAL + N_TEST]
    
    #   3) DST/분할이름/cls 폴더를 만들고 shutil.copy2 로 복사
    for split_name, split_files in [("train", train_files), ("val", val_files), ("test", test_files)]:
        dst_dir = DST / split_name / cls
        dst_dir.mkdir(parents=True, exist_ok=True)
        
        for file in split_files:
            shutil.copy2(file, dst_dir / file.name)

    print(f"{cls}: 완료")


if __name__ == "__main__":
    for c in CLASSES:
        split_class(c)
