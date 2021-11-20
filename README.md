# mac-ocr-translator

## installation
- `pip install -r requirements.txt`
- `brew install imagemagick`
- `brew install tesseract`
- `brew install tesseract-lang`
- `brew install python-tk@3.9`
- git clone this repository 
- run `install.sh`
- preference - 사용자 및 그룹 - 로그인 항목 - 해당 프로그램 등록
- preference - 보안 및 개인정보보호 - 손쉬운 사용 - 해당 프로그램 등록 (termianl 혹은 IDE)
- preference - 보안 및 개인정보보호 - 화면 기록 - 해당 프로그램 등록 (termianl 혹은 IDE)

## How to use
- `cmd` + `shift` + 1

### TODO
- [x] python key event listener for screenshot
- [x] python key event that trigger screenshot
- [x] apply ocr
- [x] translator (https://github.com/ssut/py-googletrans)
- [x] overlay result
- [ ] python running in background and launch at login
- [ ] close result by key event
