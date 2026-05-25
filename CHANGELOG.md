Release Notes
---

## [2.0.0](https://github.com/AlertaDengue/pyreaddbc/compare/1.2.0...2.0.0) (2026-05-25)

### ⚠ BREAKING CHANGES

* This PR removes the need of libffi-dev which may fail on Windows SO

* fix: update setup-miniconda to v3 on CI

* feat: update release files on CI & include wheel for Windows and macOS

* fix: this commit fixes the wheels building on WindowsOS

* chore(CI): include tests on other matrix on CI

* chore(CI): include coverage

### deps

* remove cffi dependency ([#23](https://github.com/AlertaDengue/pyreaddbc/issues/23)) ([ce7743a](https://github.com/AlertaDengue/pyreaddbc/commit/ce7743acff4674eaa19bc5810d832f128add0c36))
