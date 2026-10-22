<p align="center">
  <img src="./public/yyc3-family.png" alt="YYC³ Family" width="1800" height="450" />
</p>

<h1 align="center">YYC³ OpenHarmony · Flutter SDK</h1>

<p align="center">
  <strong>言启千行代码 · 语枢万物智能</strong><br />
  基于 Flutter 3.22.0 的 OpenHarmony 平台兼容拓展 SDK
</p>

<p align="center">
  <img alt="Flutter" src="https://img.shields.io/badge/Flutter-3.22.0-02569B?logo=flutter&logoColor=white" />
  <img alt="Dart" src="https://img.shields.io/badge/Dart-3.4.0-0175C2?logo=dart&logoColor=white" />
  <img alt="OpenHarmony" src="https://img.shields.io/badge/OpenHarmony-API%2018-000000" />
  <img alt="JDK" src="https://img.shields.io/badge/JDK-17-E76F00" />
  <img alt="License" src="https://img.shields.io/badge/License-BSD%203--Clause-blue" />
</p>

<p align="center">
  <a href="https://github.com/YYC-Cube/YYC3-OpenHarmony">GitHub 主仓库</a> ·
  <a href="./README.en.md">English</a> ·
  <a href="./CHANGELOG.md">更新日志</a> ·
  <a href="./CONTRIBUTING.md">贡献指南</a>
</p>

---

## 项目概览

YYC³ OpenHarmony 是面向 OpenHarmony 生态的 Flutter SDK 兼容拓展仓库。在保持 Flutter 官方开发体验的前提下，支持 IDE 或终端通过 Flutter Tools 指令直接编译、构建、调试与发布 OpenHarmony 应用（HAP / APP）。

| 项目项 | 说明 |
| --- | --- |
| 主仓库 | [https://github.com/YYC-Cube/YYC3-OpenHarmony](https://github.com/YYC-Cube/YYC3-OpenHarmony) |
| 上游来源 | [https://github.com/flutter/flutter](https://github.com/flutter/flutter) |
| 框架基线 | Flutter 3.22.0（[sdk 基线提交](https://github.com/flutter/flutter/commit/5dcb86f68f239346676ceb1ed1ea385bd215fba1)） |
| 引擎基线 | [engine 基线提交](https://github.com/flutter/engine/commit/f6344b75dcf861d8bf1f1322780b8811f982e31a) |
| 当前适配分支 | `br_3.22.0-ohos-1.0.4` |
| 许可证 | BSD 3-Clause |

### 核心能力

| 能力域 | 能力说明 |
| --- | --- |
| 工程创建 | 支持 `app`、`module`、`plugin`、`plugin_ffi` 四类 OHOS 工程模板 |
| 构建发布 | 支持 `debug` / `profile` / `release` 三态构建，产出 HAP 与 APP 包 |
| 渲染引擎 | 支持 impeller-vulkan（默认）与 skia-gl 双渲染模式，可按工程配置切换 |
| 设备调试 | 支持设备发现、安装、运行、attach、截屏与日志采集 |
| 依赖生态 | 对接 `pub` 依赖体系与 OpenHarmony 三方库适配计划 |
| 环境治理 | 提供 `doctor` 环境自检与国内镜像加速配置 |

## 版本基线

| 组件 | 版本 / 提交 | 说明 |
| --- | --- | --- |
| Flutter Framework | 3.22.0 | 基于 Flutter 官方社区 3.22.0 构建 |
| Flutter Engine（上游） | `f6344b75dcf861d8bf1f1322780b8811f982e31a` | 引擎基线提交 |
| Flutter Engine（OHOS） | `2317265cd53ac33c71f76ecc22cc06d97309b6db` | OpenHarmony 适配引擎提交 |
| Dart SDK | 3.4.0 | 随 Flutter 3.22.0 配套 |
| DevTools | 2.34.1 | 调试与性能分析工具 |
| OpenHarmony SDK | API 20 | 默认目标（`runtimeOS=OpenHarmony`），CI 已验证 |
| HarmonyOS SDK | 5.1.0（API 18） | HarmonyOS NEXT 目标（`runtimeOS=HarmonyOS`），需 `openharmony` + `hms` 双组件 |
| JDK | 17 | 构建工具链依赖 |

## 仓库结构

```text
YYC3-OpenHarmony/
├── app_build/          # 构建辅助脚本（build_dill / debug / release / config）
├── bin/                # flutter、dart 启动脚本，以及 SDK 缓存与版本基线文件
├── dev/                # 框架开发脚本、基准测试与集成测试
├── examples/           # OHOS 平台示例工程（hello_world、platform_view、texture 等 10 个）
├── packages/           # Flutter 框架包（flutter、flutter_tools、flutter_test 等 9 个）
├── public/             # 品牌与文档静态资源
├── release-notes/      # 版本变更记录与 Breaking Changes
├── .github/            # CI/CD 流水线、Issue / PR 模板、Dependabot 配置
├── README.md           # 中文说明文档
└── README.en.md        # 英文说明文档
```

- `packages/`：`flutter`、`flutter_driver`、`flutter_goldens`、`flutter_localizations`、`flutter_test`、`flutter_tools`、`flutter_web_plugins`、`fuchsia_remote_debug_protocol`、`integration_test`
- `examples/`：`api`、`flutter_view`、`hello_world`、`image_list`、`layers`、`platform_channel`、`platform_channel_swift`、`platform_view`、`splash`、`texture`

## 快速开始

### 1. 环境准备

| 依赖 | 要求 |
| --- | --- |
| 开发系统 | Windows（已验证）/ Linux / macOS |
| OpenHarmony SDK | API 20（默认目标，`DEVECO_SDK_HOME` 指向 SDK 根目录） |
| HarmonyOS SDK | 5.1.0 / API 18（HarmonyOS NEXT 目标，需同时安装 `openharmony` 与 `hms` 组件） |
| IDE / 命令行工具 | DevEco Studio 5.1+ 或 command-line-tools 5.1（`ohpm`、`hvigor`、`node`、`npm` 在 PATH） |
| JDK | 17 |

**请从[鸿蒙 SDK](https://developer.huawei.com/consumer/cn/develop)下载配套开发工具。**

下列环境变量配置，类 Unix 系统（Linux、macOS）可直接参照配置；Windows 请在“编辑系统环境变量”中设置。

### 2. 获取代码

```sh
# YYC³ 主仓库
git clone -b br_3.22.0-ohos-1.0.4 https://github.com/YYC-Cube/YYC3-OpenHarmony.git

# 如需跟进上游，可添加上游远程仓库
cd YYC3-OpenHarmony
git remote add upstream https://github.com/YanYuCloud/openharmony.git
```

### 3. 配置环境变量

```sh
# 依赖缓存（自定义路径）
export PUB_CACHE=D:/PUB

# 国内镜像加速
export PUB_HOSTED_URL=https://pub.flutter-io.cn
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn

# SDK bin 目录
export PATH=<YYC3-OpenHarmony path>/bin:$PATH

# HarmonyOS SDK（macOS 示例）
export TOOL_HOME=/Applications/DevEco-Studio.app/Contents
export DEVECO_SDK_HOME=$TOOL_HOME/sdk
export PATH=$TOOL_HOME/tools/ohpm/bin:$PATH
export PATH=$TOOL_HOME/tools/hvigor/bin:$PATH
export PATH=$TOOL_HOME/tools/node/bin:$PATH
```

### 4. 环境自检

```sh
flutter doctor -v
```

**Flutter** 与 **OpenHarmony** 均应显示 `ok`；若提示缺少环境，按提示补齐即可。

### 5. 创建工程与构建

编译产物位于 `<projectName>/ohos/entry/build/default/outputs/default/entry-default-signed.hap`。

```sh
# 创建工程
flutter create --platforms ohos <projectName>

# 进入工程根目录后构建
# 默认从云端获取 engine 产物，无需 --local-engine 参数
flutter build hap --target-platform ohos-arm64 --debug
flutter build hap --target-platform ohos-arm64 --profile
flutter build hap --target-platform ohos-arm64 --release
```

如需使用本地 engine 产物：

```sh
flutter build hap --target-platform ohos-arm64 --release \
  --local-engine=src/out/ohos_release_arm64 \
  --local-engine-host=src/out/host_release
```

engine 产物均在 `src/out` 路径下：

- 目标产物：`ohos_debug_unopt_arm64`、`ohos_profile_arm64`、`ohos_release_arm64`
- 宿主产物：`host_debug_unopt`、`host_profile`、`host_release`

**渲染模式开关**：当前 Flutter OHOS 平台支持 impeller-vulkan（默认）与 skia-gl。开关位于 `ohos/entry/src/main/resources/rawfile/buildinfo.json5`（`flutter create` 后首次位于 `profile` 目录，首次 `run` 或 `build` 后迁移至 `rawfile` 目录）。

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

新建工程默认开启 impeller。旧工程可将该文件复制到对应 `rawfile` 目录并修改 `value`；若未添加开关，默认开启 enable-impeller。

### 6. 运行、安装与打包

```sh
# 发现设备
flutter devices

# 直接运行（debug）
flutter run --debug -d <device-id>

# 安装 HAP
hdc -t <deviceId> install <hap file path>

# 构建 APP 包
flutter build app --release
```

## 已兼容 OpenHarmony 开发的指令列表

| 指令名称 | 指令描述 | 使用说明 |
| --- | --- | --- |
| doctor | 环境检测 | `flutter doctor` |
| config | 环境配置 | `flutter config --<key> <value>` |
| create | 创建新项目 | `flutter create --platforms ohos,android,ios --org <org> <appName>` |
| create | 创建 module 模板 | `flutter create -t module <module_name>` |
| create | 创建 plugin 模板 | `flutter create -t plugin --platforms ohos,android,ios <plugin_name>` |
| create | 创建 plugin_ffi 模板 | `flutter create -t plugin_ffi --platforms ohos,android,ios <plugin_name>` |
| devices | 已连接设备查找 | `flutter devices` |
| install | 应用安装 | `flutter install -t <deviceId> <hap文件路径>` |
| assemble | 资源打包 | `flutter assemble` |
| build | 测试应用构建 | `flutter build hap --debug [--target-platform ohos-arm64] [--local-engine=<兼容ohos的debug engine产物路径>]` |
| build | 正式应用构建 | `flutter build hap --release [--target-platform ohos-arm64] [--local-engine=<兼容ohos的release engine产物路径>]` |
| run | 应用运行 | `flutter run [--local-engine=<兼容ohos的engine产物路径>]` |
| attach | 调试模式 | `flutter attach` |
| screenshot | 截屏 | `flutter screenshot` |
| pub | 获取依赖 | `flutter pub get` |
| clean | 清除项目依赖 | `flutter clean` |
| cache | 清除全局缓存数据 | `flutter pub cache clean` |

附：[Flutter 三方库适配计划](https://docs.qq.com/sheet/DVVJDWWt1V09zUFN2)

## 工程化与质量保障

### CI 流水线

仓库内置 GitHub Actions 工作流，覆盖以下环节：

| 工作流 | 作用 |
| --- | --- |
| `ci.yml` | 仓库完整性校验（版本基线、JSON/YAML 语法、相对链接、上游专用配置防回归）与手动 SDK 冒烟测试 |
| `build.yml` | 自托管 Runner 上构建示例工程 HAP，产出可下载产物与 SHA-256 校验值 |
| `labeler.yml` | PR 自动标签 |
| `lock.yaml` | 已关闭 Issue 自动锁定 |
| `no-response.yaml` | 长时间无响应 Issue 治理 |
| `scorecards-analysis.yml` | 开源安全评分（OpenSSF Scorecard） |

### 自托管 Runner 接入

`build.yml` 仅在注册了 `self-hosted` + `ohos` 标签的 Runner 上运行，用于真实构建 HAP。Runner 需具备：

| 依赖 | 要求 |
| --- | --- |
| 操作系统 | Windows（已验证）/ Linux / macOS |
| JDK | 17 |
| OpenHarmony SDK | API 20，并导出 `DEVECO_SDK_HOME`（可选 `OHOS_BASE_SDK_HOME`） |
| HarmonyOS SDK | 5.1.0 / API 18，`<sdk>/<api>/` 下同时含 `openharmony` 与 `hms` |
| 命令行工具 | command-line-tools 5.1（`ohpm`、`hvigor`、`node`、`npm` 在 PATH） |
| 设备工具 | `hdc` 在 PATH |
| 可选仓库变量 | `PUB_HOSTED_URL`、`FLUTTER_STORAGE_BASE_URL`、`FRAMEWORK_VERSION`、`OPENHARMONY_API`、`ENABLE_HARMONYOS_TARGET` |

> Windows Runner 注意：系统级 `npm.cmd` 若被 pnpm 垫片覆盖，`hvigorw` 与 Flutter 的 hvigor 插件安装都会失败。请确保 PATH 中最先出现的 Node 来自完整安装（例如 DevEco 自带 `tools/node`），并设置 `NODE_HOME`。

### 双目标构建矩阵

`build.yml` 负责分发，`build-hap.yml` 为可复用工作流，按 `target_os` 切换示例工程配置：

| 目标 | runtimeOS | SDK | 示例配置来源 |
| --- | --- | --- | --- |
| `openharmony` | OpenHarmony | API 20（`compileSdkVersion`/`targetSdkVersion`/`compatibleSdkVersion` = 20） | 仓库内 `build-profile.json5` |
| `harmonyos` | HarmonyOS | 5.1.0(18) | `build-profile.harmonyos.json5` 等三个同名变体 |

触发方式：`workflow_dispatch` 选择 `target_os`（`both` / `openharmony` / `harmonyos`）、`release` / `profile` / `debug`、`ohos-arm64` / `ohos-x64` 与示例工程；推送 `v*` 标签时按 `both` 执行。

- HarmonyOS NEXT 分支默认关闭：安装 HarmonyOS SDK 后，设置仓库变量 `ENABLE_HARMONYOS_TARGET=true` 才会执行；未开启时会有一条显式 warning，不会产生“假绿”。
- 产物命名：`hap-<target_os>-<mode>-<platform>`，压缩包内附 `SHA256SUMS`，运行摘要同时记录 commit、大小与 SHA-256。

### 签名与验收状态

当前流水线以 `--no-codesign` 构建，产物为 **unsigned HAP**，仅用于编译验证，**不能直接安装到设备**。生产交付还需补齐：

1. 签名材料（HarmonyOS NEXT 需 AGC 证书/profile；OpenHarmony 需对应签名证书），通过 Secrets 注入或使用 `hap-sign-tool` 在构建后签名；
2. 真机/模拟器验收：`hdc install` + 启动冒烟，作为发布阻断条件；
3. 产物证明：签名后重新生成 SHA-256 并归档，必要时增加 SBOM 与构建来源证明。

### 五维质量审计基线

| 维度 | 审计关注点 | 本项目实践 |
| --- | --- | --- |
| 时间维度 | 构建耗时、加载性能、响应时延 | 云端 engine 产物复用、增量构建、profile 模式性能采样 |
| 空间维度 | 代码组织、组件边界、资源占用 | `packages/` 与 `examples/` 分层，SDK 与示例解耦 |
| 属性维度 | 性能、安全、可维护性、可复用性 | BSD 3-Clause 许可、Scorecards 安全扫描、依赖锁定 |
| 事件维度 | 交互事件、异常处理、状态管理 | 完整命令链路（create → build → run → install）闭环 |
| 关联维度 | 组件依赖、API 集成、生态连接 | 对接 pub 生态与 OpenHarmony 三方库适配计划 |

## 版本演进与升级指导

### Flutter OH 版本演进规划和分支策略

您可以在 [Flutter OH 版本演进规划和分支策略](https://gitcode.com/openharmony-tpc/flutter_flutter/wiki/Flutter-OH%E7%89%88%E6%9C%AC%E6%BC%94%E8%BF%9B%E8%A7%84%E5%88%92%E5%92%8C%E5%88%86%E6%94%AF%E7%AD%96%E7%95%A5.md) 中了解 OpenHarmony 适配版本的说明。

### 升级指导

1. 从鸿蒙 3.7.12 升级到 3.22.0
   - 环境依赖：两者环境配置一致，无需额外修改
   - 官方特性新增与变更请参考 [Release Notes](https://docs.flutter.dev/release/release-notes)
   - 官方兼容性变更请参考 [升级指导](https://docs.flutter.dev/release/breaking-changes)
   - 兼容性变更说明请参考 [变更说明](./release-notes/changelog/Flutter3.7_to_3.22_Breaking-changes.md)
   - 渲染引擎：新增 impeller-vulkan 模式（默认，可切换为 skia-gl）
   - 三方库：
     - 纯 Dart 库请升级到指定版本以支持 3.22.0
     - [openharmony-tpc/flutter_packages](https://gitcode.com/openharmony-tpc/flutter_packages/blob/master/README.md) 中的 package 已在 3.22.0 版本完成一轮可用性测试，如有问题请创建 issue 跟踪解决

2. 从 Android / iOS 迁移到鸿蒙适配 3.22.0 版本，请参考其余指导文档。

## 开发文档

- [参考文档](https://gitcode.com/openharmony-tpc/flutter_samples/tree/master/ohos/docs)
- [版本变更记录](./CHANGELOG.md)
- [Release Notes](./release-notes/)

## 常见问题

1. 切换 `FLUTTER_STORAGE_BASE_URL` 后需删除 `<flutter>/bin/cache` 目录，并在项目中执行 `flutter clean` 后再运行。

2. 若出现报错：`The SDK license agreement is not accepted`，参考执行以下命令后再次编译：

   ```sh
   ./ohsdkmgr install ets:9 js:9 native:9 previewer:9 toolchains:9 --sdk-directory='/home/xc/code/sdk/ohos-sdk/' --accept-license
   ```

3. 如果你使用的是 DevEco Studio 的 Beta 版本，编译工程时遇到 “must have required property 'compatibleSdkVersion', location: demo/ohos/build-profile.json5:17:11” 错误，请参考《DevEco Studio 环境配置指导.docx》中的“6 创建工程和运行 Hello World”【配置插件】章节修改 `hvigor/hvigor-config.json5` 文件。

4. 若提示安装报错：`fail to verify pkcs7 file`，请执行指令：

   ```sh
   hdc shell param set persist.bms.ohCert.verify true
   ```

5. Linux 虚拟机通过 hdc 无法直接发现 OpenHarmony 设备。

   解决方案：在 Windows 宿主机中开启 hdc server，具体指令如下：

   ```sh
   hdc kill
   hdc -s serverIP:8710 -m
   ```

   在 Linux 中配置环境变量：

   ```sh
   HDC_SERVER=<serverIP>
   HDC_SERVER_PORT=8710
   ```

   配置完成后 Flutter SDK 可以通过 hdc server 完成设备连接，也可参考[官方指导](https://docs.openharmony.cn/pages/v5.0/zh-cn/device-dev/subsystems/subsys-toolchain-hdc-guide.md/#hdc-client%E5%A6%82%E4%BD%95%E8%BF%9C%E7%A8%8B%E8%AE%BF%E9%97%AEhdc-server)。

6. 构建 HAP 任务时报错：`Error: The hvigor depends on the npmrc file. Configure the npmrc file first.`

   请在用户目录 `~` 下创建文件 `.npmrc`，该配置也可参考 [DevEco Studio 官方文档](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/environment_config-0000001052902427-V3)，编辑内容如下：

   ```
   registry=https://repo.huaweicloud.com/repository/npm/
   @ohos:registry=https://repo.harmonyos.com/npm/
   ```

7. 查日志时存在日志丢失现象。

   解决方案：关闭全局日志，只打开自己领域的日志。

   ```sh
   # 步骤一：关闭所有领域的日志打印（部分特殊日志无法关闭）
   hdc shell hilog -b X

   # 步骤二：只打开自己领域的日志
   hdc shell hilog <level> -D <domain>
   ```

   其中 `<level>` 为日志打印级别：`D/I/W/E/F`；`<domain>` 为 Tag 前面的数字。

   示例：打印 `A00000/XComFlutterOHOS_Native` 的日志，需设置 `hdc shell hilog -b D -D A00000`。

   注：以上设置在机器重启后会失效，如需继续使用需要重新设置。

8. 若 API 11 Beta1 版本的机器上无法启动 debug 签名的应用，可以通过将签名换成正式签名，或在手机端打开开发者模式解决（步骤：设置 -> 通用 -> 开发者模式）。

9. 如果报 `Invalid CEN header (invalid zip64 extra data field size)` 异常，请更换 JDK 版本，参见 [JDK-8313765](https://bugs.openjdk.org/browse/JDK-8313765)。

10. 运行 debug 版本的 Flutter 应用用到鸿蒙设备后报错（release 和 profile 版本正常）。

    1. 报错信息：`Error while initializing the Dart VM: Wrong full snapshot version, expected '8af474944053df1f0a3be6e6165fa7cf' found 'adb4292f3ec25074ca70abcd2d5c7251'`
    2. 解决方案：依次执行以下操作
       1. 设置环境变量 `export FLUTTER_STORAGE_BASE_URL=https://flutter-ohos.obs.cn-south-1.myhuaweicloud.com`
       2. 删除 `<flutter>/bin/cache` 目录下的缓存
       3. 执行 `flutter clean`，清除项目编译缓存
       4. 运行 `flutter run -d $DEVICE --debug`
    3. 补充信息：运行 Android 或 iOS 出现类似错误，也可以尝试还原环境变量 `FLUTTER_STORAGE_BASE_URL`，清除缓存后重新运行。

11. Beta2 版本的 ROM 更新后，不再支持申请有执行权限的匿名内存，导致 debug 运行闪退。

    1. 解决方案：更新 `flutter_flutter` 到 `a44b8a6d`（2024-07-25）之后的版本。
    2. 关键日志：

    ```
    #20 at attachToNative (oh_modules/.ohpm/@ohos+flutter_ohos@g8zhdaqwu8gotysbmqcstpfpcpy=/oh_modules/@ohos/flutter_ohos/src/main/ets/embedding/engine/FlutterNapi.ets:78:32)
    #21 at attachToNapi (oh_modules/.ohpm/@ohos+flutter_ohos@g8zhdaqwu8gotysbmqcstpfpcpy=/oh_modules/@ohos/flutter_ohos/src/main/ets/embedding/engine/FlutterEngine.ets:144:5)
    #22 at init (oh_modules/.ohpm/@ohos+flutter_ohos@g8zhdaqwu8gotysbmqcstpfpcpy=/oh_modules/@ohos/flutter_ohos/src/main/ets/embedding/engine/FlutterEngine.ets:133:7)
    ```

12. 构建 HAP 命令直接执行 `flutter build hap` 即可，不再需要 `--local-engine` 参数，直接从云端获取编译产物。

13. 配置环境完成后执行 flutter 命令出现闪退。

    1. 解决方案：Windows 环境中添加 git 环境变量配置。

    ```
    export PATH=<git path>/cmd:$PATH
    ```

14. 执行 `flutter pub cache clean` 正常，执行 `flutter clean` 报错，按照报错信息执行 update 命令也没有效果。

    1. 解决方案：通过注释掉 `build.json5` 文件中的配置规避。
    2. 报错信息：

    ```
    #Parse ohos module. json5 error: Exception: Can not found module.json5 at
    #D:\pub_cache\git\flutter_packages-b00939bb44d018f0710d1b080d91dcf4c34ed06\packages\video_player\video_player_ohos\ohossrc\main\module.json5.
    #You need to update the Flutter plugin project structure.
    #See
    #https://gitcode.com/openharmony-tpc/flutter_samples/blob/master/ohos/docs/09_specifications/update-flutter-plugin-structure.md
    ```

15. 执行 `flutter build hap` 时遇到路径校验报错。

    1. 解决方案：
       - 打开 DevEco 安装路径 `D:\DevEco Studio\tools\hvigor\hvigor-ohos-plugin\res\schemas` 下的 `ohos-project-build-profile-schema.json` 文件。
       - 在该文件中找到包含 `"pattern": "^(\\./|\\.\\./)[\\s\\S]+$"` 的行，并删除此行。
    2. 报错信息：

    ```
    #hvigor  ERROR: Schema validate failed.
    #        Detail: Please check the following fields.
    #instancePath: 'modules[1].scrPath',
    #keyword: 'pattern'
    #params: { pattern:'^(\\./|\\.\\./)[\\s\\S]+$' },
    #message: 'must match pattern "^(\\./|\\.\\./)[\\s\\S]+$"',
    #location: 'D:/work/videoplayerdemo/video_cannot_stop_at_background/ohos/build-profile.json:42:146'
    ```

16. 执行 `flutter build hap` 报错。

    1. 解决方案：打开 DevEco 安装路径 `D:\DevEco Studio\tools\hvigor\hvigor-ohos-plugin\src\model\module` 下的 `core-module-model-impl.js`，修改 `findBelongProjectPath` 方法（需要管理员权限，可另存为后替换）。

    ```js
    findBelongProjectPath(e) {
      if (e === path_1.default.dirname(e)) {
         return this.parentProject.getProjectDir()
      }
    }
    ```

    2. 报错信息：

    ```
    # hvigor  ERROR: Cannot find belonging project path for module at D:\.
    # hvigor  ERROR:  BUILD FAILED in 2s 556ms.
    #Running Hvigor task assembleHap...
    #Oops; flutter has exited unexpectedly: "ProcessException: The command failed
    #  <Command: hvigorw --mode module -p module=video_player_ohos@default -p product=default assmbleHar --no-daemon"
    #A crash report has been written to D:\work\videoplayerdemo\video_cannot_stop_at_background\flutter_03.log.
    ```

17. DevEco Studio 5.0.3.600 Beta3（Windows 版本）编译 Flutter 应用报错。

    1. 解决方案：更新 `flutter_flutter` 到 `c6fbac2b`（2024-08-09）之后的版本。
    2. 关键日志：

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

18. 在 `.ohos` 项目执行 `flutter clean` 报错，然后再执行 `flutter pub get` 也报错。

    1. 解决方案：删除 `.ohos` 文件夹，重新 `flutter pub get` 即可。
    2. 报错信息：

    ```
    Oops; flutter has exited unexpectedly: "PathNotFoundException: Cannot open file, path = 'D:\code\.ohos\build-profile.json5' (OS Error: 系统找不到指定的文件。，error = 2)".
    A crash report has been written to D:\code\flutter_01.log.
    ```

19. 模拟器执行时发生白屏、崩溃等现象。

    1. 模拟器只支持 Mac（arm64），还不支持 Mac（x86）和 Windows。
    2. 模拟器暂不支持 Vulkan，请尝试构建步骤中的渲染模式开关，关闭 impeller 后重试。

20. Flutter profile 模式下编译或运行失败。

    1. 请在 OHOS 项目 `build_profile.json5` 中添加 `buildModeSet` 字段，可参考 [complex_layout](https://gitee.com/harmonycommando_flutter/flutter/blob/oh-3.22.0/dev/benchmarks/complex_layout/ohos/build-profile.json5)。
    2. 报错信息：

    ```
    hvigor ERROR: Build mode 'profile' used in command line is not declared in buildModeSet in /xxx/example/ohos/build-profile.json5.
    ```

[更多 FAQ](https://gitcode.com/openharmony-tpc/flutter_samples/blob/master/ohos/docs/08_FAQ/README.md)

## 远程仓库与分支协作

| 远程仓库 | 地址 | 用途 |
| --- | --- | --- |
| `origin` | `https://github.com/YanYuCloud/openharmony.git` | 上游同步与变更追踪 |
| `yyc3` | `https://github.com/YYC-Cube/YYC3-OpenHarmony.git` | YYC³ 主仓库，承载适配与发布 |

```sh
# 同步上游
git fetch origin
git fetch yyc3

# 推送适配成果到 YYC³ 主仓库
git push yyc3 br_3.22.0-ohos-1.0.4
```

## 贡献

欢迎参与共建。提交代码前请阅读 [贡献指南](./CONTRIBUTING.md) 与 [行为准则](./CODE_OF_CONDUCT.md)，并通过 Issue 模板反馈问题或提出需求。

## 许可证

本项目遵循 [BSD 3-Clause License](./LICENSE)。上游 Flutter 项目版权归 Google LLC 所有。
