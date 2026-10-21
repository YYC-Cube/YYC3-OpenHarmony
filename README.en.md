<p align="center">
  <img src="./public/yyc3-family.png" alt="YYC³ Family" width="1800" height="450" />
</p>

<h1 align="center">YYC³ OpenHarmony · Flutter SDK</h1>

<p align="center">
  <strong>Words inspire thousands of lines of code · Language pivots the intelligence of all things</strong><br />
  A Flutter 3.22.0 based SDK extension for the OpenHarmony platform
</p>

<p align="center">
  <img alt="Flutter" src="https://img.shields.io/badge/Flutter-3.22.0-02569B?logo=flutter&logoColor=white" />
  <img alt="Dart" src="https://img.shields.io/badge/Dart-3.4.0-0175C2?logo=dart&logoColor=white" />
  <img alt="OpenHarmony" src="https://img.shields.io/badge/OpenHarmony-API%2018-000000" />
  <img alt="JDK" src="https://img.shields.io/badge/JDK-17-E76F00" />
  <img alt="License" src="https://img.shields.io/badge/License-BSD%203--Clause-blue" />
</p>

<p align="center">
  <a href="https://github.com/YYC-Cube/YYC3-OpenHarmony">GitHub Repository</a> ·
  <a href="./README.md">简体中文</a> ·
  <a href="./CHANGELOG.md">Changelog</a> ·
  <a href="./CONTRIBUTING.md">Contributing</a>
</p>

---

## Overview

YYC³ OpenHarmony is a compatible extension of the Flutter SDK for the OpenHarmony ecosystem. While keeping the official Flutter developer experience, it supports building, debugging, and releasing OpenHarmony applications (HAP / APP) through Flutter Tools in an IDE or terminal.

| Item | Description |
| --- | --- |
| Main repository | [https://github.com/YYC-Cube/YYC3-OpenHarmony](https://github.com/YYC-Cube/YYC3-OpenHarmony) |
| Upstream source | [https://github.com/flutter/flutter](https://github.com/flutter/flutter) |
| Framework baseline | Flutter 3.22.0 ([sdk baseline commit](https://github.com/flutter/flutter/commit/5dcb86f68f239346676ceb1ed1ea385bd215fba1)) |
| Engine baseline | [engine baseline commit](https://github.com/flutter/engine/commit/f6344b75dcf861d8bf1f1322780b8811f982e31a) |
| Current branch | `br_3.22.0-ohos-1.0.4` |
| License | BSD 3-Clause |

### Core capabilities

| Capability | Description |
| --- | --- |
| Project scaffolding | `app`, `module`, `plugin`, and `plugin_ffi` OHOS project templates |
| Build & release | `debug` / `profile` / `release` builds producing HAP and APP packages |
| Rendering engine | impeller-vulkan (default) and skia-gl, switchable per project |
| Device debugging | Device discovery, install, run, attach, screenshot, and log collection |
| Package ecosystem | `pub` dependency ecosystem and the OpenHarmony third-party adaptation plan |
| Environment governance | `doctor` environment self-check and domestic mirror acceleration |

## Version baseline

| Component | Version / Commit | Notes |
| --- | --- | --- |
| Flutter Framework | 3.22.0 | Built on the official Flutter 3.22.0 community release |
| Flutter Engine (upstream) | `f6344b75dcf861d8bf1f1322780b8811f982e31a` | Engine baseline commit |
| Flutter Engine (OHOS) | `2317265cd53ac33c71f76ecc22cc06d97309b6db` | OpenHarmony adapted engine commit |
| Dart SDK | 3.4.0 | Bundled with Flutter 3.22.0 |
| DevTools | 2.34.1 | Debugging and profiling tools |
| HarmonyOS SDK | API 18 | DevEco Studio 5.1 or command-line-tools 5.1 |
| JDK | 17 | Required by the build toolchain |

## Repository layout

```text
YYC3-OpenHarmony/
├── app_build/          # Build helper scripts (build_dill / debug / release / config)
├── bin/                # flutter and dart launchers, SDK cache and version baselines
├── dev/                # Framework development scripts, benchmarks and integration tests
├── examples/           # OHOS sample projects (hello_world, platform_view, texture, etc.)
├── packages/           # Flutter framework packages (flutter, flutter_tools, flutter_test, etc.)
├── public/             # Branding and documentation assets
├── release-notes/      # Release notes and breaking changes
├── .github/            # CI/CD workflows, issue / PR templates, Dependabot configuration
├── README.md           # Chinese documentation
└── README.en.md        # English documentation
```

- `packages/`: `flutter`, `flutter_driver`, `flutter_goldens`, `flutter_localizations`, `flutter_test`, `flutter_tools`, `flutter_web_plugins`, `fuchsia_remote_debug_protocol`, `integration_test`
- `examples/`: `api`, `flutter_view`, `hello_world`, `image_list`, `layers`, `platform_channel`, `platform_channel_swift`, `platform_view`, `splash`, `texture`

## Quick start

### 1. Prerequisites

| Dependency | Requirement |
| --- | --- |
| Development OS | Linux / macOS / Windows |
| HarmonyOS SDK | API 18 |
| IDE / CLI tools | DevEco Studio 5.1 or command-line-tools 5.1 (5.1.0 Beta1 or later recommended) |
| JDK | 17 |

**Download the matching development tools from the [HarmonyOS SDK](https://developer.huawei.com/consumer/cn/develop).**

The environment variable examples below apply directly to Unix-like systems (Linux, macOS). On Windows, configure them in “Edit system environment variables”.

### 2. Get the source

```sh
# YYC³ main repository
git clone -b br_3.22.0-ohos-1.0.4 https://github.com/YYC-Cube/YYC3-OpenHarmony.git

# Optionally add the upstream remote for tracking
cd YYC3-OpenHarmony
git remote add upstream https://github.com/YanYuCloud/openharmony.git
```

### 3. Configure environment variables

```sh
# Dependency cache (custom path)
export PUB_CACHE=D:/PUB

# Domestic mirror acceleration
export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn

# SDK bin directory
export PATH=<YYC3-OpenHarmony path>/bin:$PATH

# HarmonyOS SDK (macOS example)
export TOOL_HOME=/Applications/DevEco-Studio.app/Contents
export DEVECO_SDK_HOME=$TOOL_HOME/sdk
export PATH=$TOOL_HOME/tools/ohpm/bin:$PATH
export PATH=$TOOL_HOME/tools/hvigor/bin:$PATH
export PATH=$TOOL_HOME/tools/node/bin:$PATH
```

### 4. Self-check

```sh
flutter doctor -v
```

Both **Flutter** and **OpenHarmony** should be marked `ok`. If either reports a missing environment, follow the prompts to complete it.

### 5. Create and build

The build artifact is located at `<projectName>/ohos/entry/build/default/outputs/default/entry-default-signed.hap`.

```sh
# Create a project
flutter create --platforms ohos <projectName>

# Build from the project root
# Engine artifacts are fetched from the cloud by default; --local-engine is optional
flutter build hap --target-platform ohos-arm64 --debug
flutter build hap --target-platform ohos-arm64 --profile
flutter build hap --target-platform ohos-arm64 --release
```

To use local engine artifacts:

```sh
flutter build hap --target-platform ohos-arm64 --release \
  --local-engine=src/out/ohos_release_arm64 \
  --local-engine-host=src/out/host_release
```

Engine artifacts live under `src/out`:

- Target artifacts: `ohos_debug_unopt_arm64`, `ohos_profile_arm64`, `ohos_release_arm64`
- Host artifacts: `host_debug_unopt`, `host_profile`, `host_release`

**Rendering mode switch**: Flutter OHOS currently supports impeller-vulkan (default) and skia-gl. The switch lives in `ohos/entry/src/main/resources/rawfile/buildinfo.json5` (located in the `profile` directory after `flutter create`, and moved to `rawfile` after the first `run` or `build`).

```json
{
  "string": [
    {
      "name": "enable_impeller",
      "value": "true"
    }
  ]
}
```

New projects enable impeller by default. For existing projects, copy this file into the corresponding `rawfile` directory and change the `value`; if the switch is absent, enable-impeller is enabled by default.

### 6. Run, install and package

```sh
# Discover devices
flutter devices

# Run directly (debug)
flutter run --debug -d <device-id>

# Install a HAP
hdc -t <deviceId> install <hap file path>

# Build an APP package
flutter build app --release
```

## Compatible command list developed by OpenHarmony

| Command | Description | Usage |
| --- | --- | --- |
| doctor | Environment detection | `flutter doctor` |
| config | Environment configuration | `flutter config --<key> <value>` |
| create | Create a new project | `flutter create --platforms ohos,android,ios --org <org> <appName>` |
| create | Create a module template | `flutter create -t module <module_name>` |
| create | Create a plugin template | `flutter create -t plugin --platforms ohos,android,ios <plugin_name>` |
| create | Create a plugin_ffi template | `flutter create -t plugin_ffi --platforms ohos,android,ios <plugin_name>` |
| devices | Discover connected devices | `flutter devices` |
| install | Install an application | `flutter install -t <deviceId> <hap file path>` |
| assemble | Resource packaging | `flutter assemble` |
| build | Test application build | `flutter build hap --debug [--target-platform ohos-arm64] [--local-engine=<ohos-compatible debug engine artifact path>]` |
| build | Release application build | `flutter build hap --release [--target-platform ohos-arm64] [--local-engine=<ohos-compatible release engine artifact path>]` |
| run | Run an application | `flutter run [--local-engine=<ohos-compatible engine artifact path>]` |
| attach | Debug mode | `flutter attach` |
| screenshot | Screenshot | `flutter screenshot` |
| pub | Fetch dependencies | `flutter pub get` |
| clean | Clear project dependencies | `flutter clean` |
| cache | Clear global cache data | `flutter pub cache clean` |

See also: [Flutter third-party library adaptation plan](https://docs.qq.com/sheet/DVVJDWWt1V09zUFN2)

## Engineering and quality assurance

### CI workflows

| Workflow | Purpose |
| --- | --- |
| `ci.yml` | Repository integrity checks (version baselines, JSON/YAML syntax, relative links, upstream-only config regression) and a manual SDK smoke test |
| `build.yml` | Builds a sample HAP on a self-hosted runner and publishes the artifact with a SHA-256 checksum |
| `labeler.yml` | Automatic PR labeling |
| `lock.yaml` | Automatic locking of closed issues |
| `no-response.yaml` | Stale issue governance |
| `scorecards-analysis.yml` | OpenSSF Scorecard security analysis |

### Self-hosted runner

`build.yml` only runs on a runner labeled `self-hosted` and `ohos` to produce a real HAP. The runner requires:

| Dependency | Requirement |
| --- | --- |
| OS | Linux or macOS (bash required) |
| JDK | 17 |
| HarmonyOS SDK | API 18 with `DEVECO_SDK_HOME` exported |
| CLI tools | command-line-tools 5.1 (`ohpm`, `hvigor`, `node` on PATH) |
| Device tooling | `hdc` on PATH |
| Optional repository variables | `PUB_HOSTED_URL`, `FLUTTER_STORAGE_BASE_URL` |

Triggers: `workflow_dispatch` with selectable `release` / `profile` / `debug`, `ohos-arm64` / `ohos-x64`, and sample project; pushing a `v*` tag builds release automatically.

### Five-dimensional quality baseline

| Dimension | Audit focus | Practice in this repository |
| --- | --- | --- |
| Time | Build time, load performance, response latency | Cloud engine artifact reuse, incremental builds, profile-mode sampling |
| Space | Code organization, component boundaries, resource usage | Layered `packages/` and `examples/`, decoupled SDK and samples |
| Attribute | Performance, security, maintainability, reusability | BSD 3-Clause license, Scorecards scanning, dependency locking |
| Event | Interaction events, error handling, state management | Closed loop from `create` to `build`, `run`, and `install` |
| Association | Component dependencies, API integration, ecosystem links | `pub` ecosystem and the OpenHarmony third-party adaptation plan |

## Version evolution and upgrade guide

### Flutter OH version evolution and branching strategy

See [Flutter OH version evolution planning and branching strategy](https://gitcode.com/openharmony-tpc/flutter_flutter/wiki/Flutter-OH%E7%89%88%E6%9C%AC%E6%BC%94%E8%BF%9B%E8%A7%84%E5%88%92%E5%92%8C%E5%88%86%E6%94%AF%E7%AD%96%E7%95%A5.md).

### Upgrade guide

1. Upgrading from HarmonyOS 3.7.12 to 3.22.0
   - Environment: configuration is identical; no extra changes are required
   - New features and changes: see [Release Notes](https://docs.flutter.dev/release/release-notes)
   - Official compatibility changes: see [Breaking changes](https://docs.flutter.dev/release/breaking-changes)
   - Changelog: see [Flutter3.7_to_3.22_Breaking-changes.en.md](./release-notes/changelog/Flutter3.7_to_3.22_Breaking-changes.en.md)
   - Rendering engine: impeller-vulkan mode added (default, switchable to skia-gl)
   - Third-party libraries:
     - Pure Dart libraries must be upgraded to versions supporting 3.22.0
     - Packages in [openharmony-tpc/flutter_packages](https://gitcode.com/openharmony-tpc/flutter_packages/blob/master/README.md) have passed a basic usability test for 3.22.0; please file an issue if you encounter problems

2. Migrating from Android or iOS to the HarmonyOS 3.22.0 adaptation: refer to the remaining guide documents.

## Documentation

- [Reference documentation](https://gitcode.com/openharmony-tpc/flutter_samples/tree/master/ohos/docs)
- [Changelog](./CHANGELOG.md)
- [Release notes](./release-notes/)

## FAQ

1. After switching `FLUTTER_STORAGE_BASE_URL`, delete the `<flutter>/bin/cache` directory and run `flutter clean` in the project before running again.

2. If you see `The SDK license agreement is not accepted`, run the following command and build again:

   ```sh
   ./ohsdkmgr install ets:9 js:9 native:9 previewer:9 toolchains:9 --sdk-directory='/home/xc/code/sdk/ohos-sdk/' --accept-license
   ```

3. If you use a Beta version of DevEco Studio and encounter “must have required property 'compatibleSdkVersion', location: demo/ohos/build-profile.json5:17:11”, modify `hvigor/hvigor-config.json5` by referring to section “6 Create the project and run Hello World” [Configure plugins] in the *DevEco Studio Environment Configuration Guide*.

4. If installation reports `fail to verify pkcs7 file`, run:

   ```sh
   hdc shell param set persist.bms.ohCert.verify true
   ```

5. A Linux virtual machine cannot discover OpenHarmony devices through hdc directly.

   Solution: start the hdc server on the Windows host:

   ```sh
   hdc kill
   hdc -s serverIP:8710 -m
   ```

   Configure the environment variables on Linux:

   ```sh
   HDC_SERVER=<serverIP>
   HDC_SERVER_PORT=8710
   ```

   The Flutter SDK can then connect through the hdc server. See also the [official guide](https://docs.openharmony.cn/pages/v5.0/zh-cn/device-dev/subsystems/subsys-toolchain-hdc-guide.md/#hdc-client%E5%A6%82%E4%BD%95%E8%BF%9C%E7%A8%8B%E8%AE%BF%E9%97%AEhdc-server).

6. Building a HAP fails with `Error: The hvigor depends on the npmrc file. Configure the npmrc file first.`

   Create a `.npmrc` file in your home directory `~`. See the [DevEco Studio documentation](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/environment_config-0000001052902427-V3). Content:

   ```
   registry=https://repo.huaweicloud.com/repository/npm/
   @ohos:registry=https://repo.harmonyos.com/npm/
   ```

7. Logs are lost when querying logs.

   Solution: disable global logs and enable only your domain.

   ```sh
   # Step 1: disable all domain logging (some special logs cannot be disabled)
   hdc shell hilog -b X

   # Step 2: enable only your domain
   hdc shell hilog <level> -D <domain>
   ```

   `<level>` is the log level: `D/I/W/E/F`; `<domain>` is the number before the tag.

   Example: to print `A00000/XComFlutterOHOS_Native`, run `hdc shell hilog -b D -D A00000`.

   Note: these settings are lost after a device reboot and must be reapplied.

8. If a debug-signed application cannot start on an API 11 Beta1 device, switch to an official signature or enable developer mode on the device (Settings -> General -> Developer mode).

9. If you see `Invalid CEN header (invalid zip64 extra data field size)`, change the JDK version; see [JDK-8313765](https://bugs.openjdk.org/browse/JDK-8313765).

10. A debug build of the Flutter application fails on a HarmonyOS device (release and profile builds work).

    1. Error: `Error while initializing the Dart VM: Wrong full snapshot version, expected '8af474944053df1f0a3be6e6165fa7cf' found 'adb4292f3ec25074ca70abcd2d5c7251'`
    2. Solution: perform the following steps in order
       1. Set `export FLUTTER_STORAGE_BASE_URL=https://flutter-ohos.obs.cn-south-1.myhuaweicloud.com`
       2. Delete the cache under `<flutter>/bin/cache`
       3. Run `flutter clean` to clear the project build cache
       4. Run `flutter run -d $DEVICE --debug`
    3. Note: if a similar error occurs on Android or iOS, restore `FLUTTER_STORAGE_BASE_URL`, clear the cache, and run again.

11. After the Beta2 ROM update, anonymous executable memory can no longer be requested, causing debug builds to crash.

    1. Solution: update `flutter_flutter` to a version after `a44b8a6d` (2024-07-25).
    2. Key logs:

    ```
    #20 at attachToNative (oh_modules/.ohpm/@ohos+flutter_ohos@g8zhdaqwu8gotysbmqcstpfpcpy=/oh_modules/@ohos/flutter_ohos/src/main/ets/embedding/engine/FlutterNapi.ets:78:32)
    #21 at attachToNapi (oh_modules/.ohpm/@ohos+flutter_ohos@g8zhdaqwu8gotysbmqcstpfpcpy=/oh_modules/@ohos/flutter_ohos/src/main/ets/embedding/engine/FlutterEngine.ets:144:5)
    #22 at init (oh_modules/.ohpm/@ohos+flutter_ohos@g8zhdaqwu8gotysbmqcstpfpcpy=/oh_modules/@ohos/flutter_ohos/src/main/ets/embedding/engine/FlutterEngine.ets:133:7)
    ```

12. Run `flutter build hap` directly; the `--local-engine` parameter is no longer required, as artifacts are fetched from the cloud.

13. The flutter command crashes after environment configuration.

    1. Solution: add the git environment variable on Windows.

    ```
    export PATH=<git path>/cmd:$PATH
    ```

14. `flutter pub cache clean` works, but `flutter clean` fails, and the suggested update command has no effect.

    1. Solution: comment out the configuration in `build.json5`.
    2. Error:

    ```
    #Parse ohos module. json5 error: Exception: Can not found module.json5 at
    #D:\pub_cache\git\flutter_packages-b00939bb44d018f0710d1b080d91dcf4c34ed06\packages\video_player\video_player_ohos\ohossrc\main\module.json5.
    #You need to update the Flutter plugin project structure.
    #See
    #https://gitcode.com/openharmony-tpc/flutter_samples/blob/master/ohos/docs/09_specifications/update-flutter-plugin-structure.md
    ```

15. `flutter build hap` reports a path validation error.

    1. Solution:
       - Open `ohos-project-build-profile-schema.json` under `D:\DevEco Studio\tools\hvigor\hvigor-ohos-plugin\res\schemas`.
       - Find the line containing `"pattern": "^(\\./|\\.\\./)[\\s\\S]+$"` and delete it.
    2. Error:

    ```
    #hvigor  ERROR: Schema validate failed.
    #        Detail: Please check the following fields.
    #instancePath: 'modules[1].scrPath',
    #keyword: 'pattern'
    #params: { pattern:'^(\\./|\\.\\./)[\\s\\S]+$' },
    #message: 'must match pattern "^(\\./|\\.\\./)[\\s\\S]+$"',
    #location: 'D:/work/videoplayerdemo/video_cannot_stop_at_background/ohos/build-profile.json:42:146'
    ```

16. `flutter build hap` fails.

    1. Solution: open `core-module-model-impl.js` under `D:\DevEco Studio\tools\hvigor\hvigor-ohos-plugin\src\model\module` and modify the `findBelongProjectPath` method (administrator privileges required; save as and replace).

    ```js
    findBelongProjectPath(e) {
      if (e === path_1.default.dirname(e)) {
         return this.parentProject.getProjectDir()
      }
    }
    ```

    2. Error:

    ```
    # hvigor  ERROR: Cannot find belonging project path for module at D:\.
    # hvigor  ERROR:  BUILD FAILED in 2s 556ms.
    #Running Hvigor task assembleHap...
    #Oops; flutter has exited unexpectedly: "ProcessException: The command failed
    #  <Command: hvigorw --mode module -p module=video_player_ohos@default -p product=default assmbleHar --no-daemon"
    #A crash report has been written to D:\work\videoplayerdemo\video_cannot_stop_at_background\flutter_03.log.
    ```

17. DevEco Studio 5.0.3.600 Beta3 (Windows) fails to compile a Flutter application.

    1. Solution: update `flutter_flutter` to a version after `c6fbac2b` (2024-08-09).
    2. Key logs:

    ```
    hvigor ERROR: Schema validate failed.
       Detail: Please check the following fields.
       {
          instancePath: 'modules[2].srcPath',
          keyword: 'pattern',
          params: { pattern: '^(\\./|\\.\\./)[\\s\\S]+$' },
          message: 'must match pattern "^(\\./|\\.\\./)[\\s\\S]+$"',
       }
    ```

18. Running `flutter clean` in a `.ohos` project fails, and `flutter pub get` then fails too.

    1. Solution: delete the `.ohos` folder and run `flutter pub get` again.
    2. Error:

    ```
    Oops; flutter has exited unexpectedly: "PathNotFoundException: Cannot open file, path = 'D:\code\.ohos\build-profile.json5' (OS Error: The system cannot find the specified file., error = 2)".
    A crash report has been written to D:\code\flutter_01.log.
    ```

19. The emulator shows a white screen or crashes.

    1. The emulator only supports Mac (arm64), not Mac (x86) or Windows.
    2. The emulator does not support Vulkan yet; disable impeller via the rendering mode switch described above and retry.

20. Compilation or runtime fails in Flutter profile mode.

    1. Add the `buildModeSet` field to `build_profile.json5` in the OHOS project. Refer to [complex_layout](https://gitee.com/harmonycommando_flutter/flutter/blob/oh-3.22.0/dev/benchmarks/complex_layout/ohos/build-profile.json5).
    2. Error:

    ```
    hvigor ERROR: Build mode 'profile' used in command line is not declared in buildModeSet in /xxx/example/ohos/build-profile.json5.
    ```

[More FAQ](https://gitcode.com/openharmony-tpc/flutter_samples/blob/master/ohos/docs/08_FAQ/README.md)

## Remotes and branch collaboration

| Remote | URL | Purpose |
| --- | --- | --- |
| `origin` | `https://github.com/YanYuCloud/openharmony.git` | Upstream synchronization and change tracking |
| `yyc3` | `https://github.com/YYC-Cube/YYC3-OpenHarmony.git` | YYC³ main repository for adaptations and releases |

```sh
# Synchronize upstream
git fetch origin
git fetch yyc3

# Push adaptation work to the YYC³ main repository
git push yyc3 br_3.22.0-ohos-1.0.4
```

## Contributing

Contributions are welcome. Please read the [Contributing Guide](./CONTRIBUTING.md) and the [Code of Conduct](./CODE_OF_CONDUCT.md) before submitting code, and use the issue templates to report problems or request features.

## License

This project is licensed under the [BSD 3-Clause License](./LICENSE). Upstream Flutter copyright belongs to Google LLC.
