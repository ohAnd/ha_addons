---
applyTo: "**/eos_connect* **"
---

# EOS Connect Release Preparation Workflows

This document defines two complementary workflows:

1. **DEVELOP WORKFLOW** — Frequent integration of upstream develop branch changes (eos_connect_develop/)
2. **PRODUCTIVE/RELEASE WORKFLOW** — Infrequent main branch releases to production (eos_connect/)

---

## WORKFLOW 1: DEVELOP (eos_connect_develop) — Frequent Integration

### Purpose

Regularly sync wrapper with `EOS_connect` develop branch changes. This is a lightweight, frequent operation.

### Trigger Phrases

When the user says any of the following, **IMMEDIATELY** execute the full workflow without asking for confirmation:

- "prepare to commit for eos connect develop"
- "prepare for eos connect develop commit"
- "eos connect develop commit prep"
- "bump eos connect develop version"
- "prepare eos connect develop"
- "new ride" (casual trigger for next cycle)

### Agent Rules (MANDATORY)

- NEVER perform `git commit` or `git push` without explicit human confirmation.
- The exact confirmation phrase required is: `approve eos commit`
- The agent MUST show: proposed commit message, extracted version number, list of non-[AUTO] commits used
- The agent MUST NOT accept other phrasing (e.g., "looks good", "proceed")
- The agent MAY stage changes (`git add`) but MUST NOT commit until receiving exact confirmation phrase
- If any step fails, abort and report failure; do NOT retry automatically

### Workflow Steps

#### Step 1: Sync the Submodule

- Navigate to `c:\projects\ha_addons\eos_connect_develop\src`
- Run: `git pull origin develop`

#### Step 2: Check for New Configuration Parameters

- Compare `src/src/config.py` with wrapper's `config.yaml`
- For each NEW parameter found:
  - Add to `config.yaml` in `options` section (with default value, comment)
  - Add to `config.yaml` in `schema` section (with validation rules)
  - Add to `translations/en.yaml` (with UI name and description)
- Mark as EXPERIMENTAL if feature is new/untested

#### Step 3: Extract Version Information

- Get latest commits from submodule
- Find latest `[AUTO]` commit (format: "Update version to X.X.X.XXX-develop")
- Extract version number: MAJOR.MINOR.PATCH.BUILD (e.g., 0.2.33.278)

#### Step 4: Update config.yaml

- Update version field: remove "-develop" suffix (0.2.33.278-develop → 0.2.33.278)

#### Step 5: Update CHANGELOG.md

- Add entry at TOP of `eos_connect_develop\CHANGELOG.md`
- Format: `**Version X.X.X.XXX** published on YYYY-MM-DD`
- For EACH non-[AUTO] commit since last wrapper commit:
  - Add bullet point with commit message
  - Preserve GitHub issue links: `[#XXX](https://github.com/ohAnd/EOS_connect/issues/XXX)`
  - Mark experimental features clearly ("EXPERIMENTAL", "Status: experimental")
  - Skip [AUTO] commits
- User-friendly descriptions focused on "what changed for users"

#### Step 6: Stage Changes & Show Proposed Commit

- Stage: `config.yaml`, `CHANGELOG.md`, `src` submodule, `translations/en.yaml`
- Show proposed commit message (format: `eos_connect_develop: bump version to X.X.X.XXX; update changelog with [key features]`)
- Wait for: `approve eos commit` confirmation

#### Format Example:

```markdown
**Version 0.2.33.278** published on 2026-03-31

- **NEW EXPERIMENTAL FEATURE: Feed-in Price in Battery Optimization**
  Added `battery.battery_price_include_feedin` (default: OFF) to factor your feed-in tariff as an "opportunity cost"
  Fixes [PR #234](https://github.com/ohAnd/EOS_connect/pull/234)
```

---

## WORKFLOW 2: PRODUCTIVE/RELEASE (eos_connect) — Infrequent Main Branch Release

### Purpose

Prepare wrapper for production release based on main branch. Occurs less frequently than develop updates.  
**Blueprint**: Use develop workflow as foundation; add additional dependency/wrapper-level checks.

### Trigger Phrases

When the user says any of the following, **IMMEDIATELY** execute the full workflow:

- "prepare eos connect for release"
- "prepare eos connect main release"
- "eos connect production prep"
- "prepare for commit - eos connect"
- "prepare eos_connect commit"

### Agent Rules (MANDATORY)

- Same commit/push restrictions as DEVELOP workflow
- Confirmation phrase: `approve eos commit`
- Do NOT automatically stage or commit
- Show proposed commit message and all modified files
- If any step fails, abort and report; do NOT retry

### Workflow Steps (Extended from DEVELOP)

#### Steps 1-6: Same as DEVELOP workflow

- Sync submodule (to main branch, not develop)
- Check for new config parameters
- Extract version
- Update config.yaml (NO "-develop" suffix to remove - main is already released version)
- Update CHANGELOG.md (comprehensive user-facing content, mark experimental features)
- Stage changes and show proposed commit

#### ADDITIONAL Step 7: Verify Dockerfile & Dependencies (WRAPPER-LEVEL)

This is the KEY difference between develop and productive flows.

**7a: Compare Wrapper Dockerfile with Develop**

- Check `c:\projects\ha_addons\eos_connect\Dockerfile` vs. `eos_connect_develop\Dockerfile`
- Verify alignment on:
  - System packages (apk add): gcc, python3-dev, musl-dev for build tools
  - Build cleanup: `apk del --purge gcc python3-dev musl-dev` (production must not include build tools)
  - WSGI server: must be waitress (NOT gevent for ARM64 stability)
  - Python package versions: must match or exceed develop version pinning
  - New dependencies: check for new packages in develop that should be in productive
  - Examples to check: pymodbus, psutil, waitress, numpy, pandas versions

**7b: Check requirements.txt Alignment**

- Verify `eos_connect/requirements.txt` (if exists) matches packages in Dockerfile
- Verify versions are compatible with develop submodule

**7c: Check Config Parameter Coverage**

- Ensure new config parameters are documented in:
  - `config.yaml` options section (with defaults)
  - `config.yaml` schema section (with validation)
  - `translations/en.yaml` (with UI strings)
  - All three must match exactly

**7d: Mark Experimental Features in CHANGELOG**

- Features marked "EXPERIMENTAL" in develop MUST also be marked in productive CHANGELOG
- Include clear warnings about testing requirements
- Provide user guidance for evaluation periods
- Examples:
  - `battery.battery_price_include_feedin` → EXPERIMENTAL, opt-in toggle
  - `eos.pv_battery_charge_control_enabled` → EXPERIMENTAL, affects PV routing strategy

**7e: Verify Submodule Commit**

- Confirm submodule is at main branch (not develop)
- Verify version in submodule matches wrapper config.yaml version

#### Step 8: Show Complete Change Summary

Display:

```
Files Modified (NOT staged):
1. config.yaml
   - Version: X.X.X.XXX → Y.Y.Y.YYY
   - New parameters: [list]
   - Dockerfile updates: [list]

2. CHANGELOG.md
   - User-friendly release notes with experimental warnings

3. Dockerfile
   - Dependencies aligned with develop: [specific changes]
   - Build tools: gcc/python3-dev/musl-dev added
   - Cleanup stage: build tools removed
   - WSGI server: gevent→waitress

4. translations/en.yaml
   - New parameter descriptions

5. eos_connect/src (submodule)
   - Updated to: [commit hash] (main branch, v0.2.33)

Commit Message: [show full message]
```

### DEPENDENCIES TO CHECK (Productive Workflow Only)

Always verify these align between develop and productive Dockerfile:

- **System packages**: gcc, python3-dev, musl-dev (build tools)
- **Python versions**: numpy, pandas (scientific stack)
- **Web server**: waitress (not gevent)
- **MQTT**: paho-mqtt
- **Configuration**: pyyaml, ruamel.yaml
- **Optimization**: pytz, packaging
- **Forecasting**: open-meteo-solar-forecast
- **System info**: psutil
- **Inverter**: pymodbus (NEW in v0.2.33)
- **Build cleanup**: apk del must remove build tools post-installation

### Commit Message Format (Productive Release)

```
eos_connect: release vX.X.X with [headline features]; align wrapper with main branch updates

Wrapper config/dependency updates:
- Upgrade version X.X.X → Y.Y.Y
- [New parameters with experimental status]
- [Dockerfile changes if needed]
- [Translation updates]

Submodule sync (develop→main):
- eos_connect/src → vY.Y.Y main branch (commit [hash])
- Includes: [major features from this release]

Release focus:
- [User-impacting improvements]
- All changes fully backward compatible

Status: [Production-ready/Testing phase]
```

---

## General Guidelines for Both Workflows

### Configuration Parameter Documentation

1. Always add parameters to **all three locations**:
   - `config.yaml` options section
   - `config.yaml` schema section
   - `translations/en.yaml`

2. For EXPERIMENTAL features:
   - Default must be OFF (false/disabled)
   - Mark as opt-in
   - Explain in CHANGELOG what user needs to monitor
   - Provide warnings about side effects or tradeoffs

### CHANGELOG Best Practices

- **Develop**: Focus on technical accuracy, PR/issue references, what changed in code
- **Productive**: Focus on user benefits, what to expect, when to enable features, testing guidance
- Mark EXPERIMENTAL features with clear warnings
- Provide actionable guidance (e.g., "Set X to true to enable")
- Link to relevant PRs/issues

### Version Management

- **Develop**: Version format X.X.X.XXX-develop (BUILD number increments with [AUTO] commits)
- **Productive**: Version format X.X.X (remove -develop suffix, represents stable release)

---

## applyTo: "**/eos_connect\* **"

### Mandatory confirmation step

- After showing the proposed commit message the agent MUST wait for the human to send the exact phrase `approve eos commit` before performing any `git commit` or `git push`.
- If the human responds with anything else, the agent must NOT commit and should instead ask for clarification or update the proposed commit message as requested.

### Staging behaviour

- The agent should list staged files and may stage changes, but MUST NOT commit/push without the exact confirmation phrase.

### Audit and reporting

- The agent must include the extracted version number and the list of non-[AUTO] commit messages used to populate `CHANGELOG.md` in the confirmation request.

## Important: Enforcement recommendation

- To help ensure these rules are respected by any automated agent, create a repository-level git hook or CI check which blocks commits unless an environment variable `ALLOW_BOT_COMMIT=true` is explicitly set by a human step. This instructions file defines the expected behaviour but cannot enforce it without repository hooks or CI.
