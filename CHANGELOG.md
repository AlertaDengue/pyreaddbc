Release Notes
---

## [2.0.2](https://github.com/AlertaDengue/pyreaddbc/compare/2.0.1...2.0.2) (2026-05-26)

### Bug Fixes

* **release:** remove python 3.13 because it's freezing the ubuntu wheels release on x86_64 ([#29](https://github.com/AlertaDengue/pyreaddbc/issues/29)) ([2ddf08a](https://github.com/AlertaDengue/pyreaddbc/commit/2ddf08ae7ba5567ed6de301668828c0c2dd2a8d6))

## [2.0.1](https://github.com/AlertaDengue/pyreaddbc/compare/2.0.0...2.0.1) (2026-05-25)

### Bug Fixes

* **release:** release workflow should trigger publish too ([#26](https://github.com/AlertaDengue/pyreaddbc/issues/26)) ([9c48298](https://github.com/AlertaDengue/pyreaddbc/commit/9c48298f1b26722b04a12b7e0a6e360c1c0444af))

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
