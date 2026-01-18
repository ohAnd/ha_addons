---
applyTo: "**/eos_connect_develop/**"
---

# EOS Connect Develop Commit Preparation Workflow

## Trigger Phrases

When the user says any of the following, **IMMEDIATELY** execute the full workflow without asking for confirmation:

- "prepare to commit for eos connect develop"
- "prepare for eos connect develop commit"
- "eos connect develop commit prep"
- "bump eos connect develop version"
- "prepare eos connect develop"

## Workflow Overview

The workflow will automatically:

1. Sync submodule with develop branch
2. Extract version from latest [AUTO] commit
3. Update config.yaml version (remove -develop suffix)
4. Update CHANGELOG.md with new entries
5. Stage all changes and show proposed commit message

## Agent Rules (MANDATORY)

- NEVER perform `git commit` or `git push` without explicit human confirmation.
- The exact confirmation phrase required is: "approve eos commit"
- The agent MUST show the full proposed commit message, the extracted version number, and the list of non-[AUTO] commits used to populate `CHANGELOG.md`, and then wait for a human message that matches the confirmation phrase exactly before performing any commit or push.
- The agent MUST NOT accept any other phrasing or implicit approvals (for example, "looks good" or "proceed").
- The agent MAY stage changes (`git add`) to prepare a commit, but MUST NOT run `git commit` or `git push` until it has received the exact confirmation phrase.
- If any step fails, the agent must abort the workflow and report the failure; do not attempt automatic retries that result in changes to git history.

## Workflow Steps

Execute the following steps automatically:

## Step 1: Sync the Submodule

- Navigate to `c:\projects\ha_addons\eos_connect_develop\src`
- Run: `git pull origin develop` to sync the submodule with the latest changes

## Step 2: Check for New Configuration Parameters

- Compare `src/src/config.py` with `config.yaml` to identify any new parameters
- For each new parameter found:
  - Add to `config.yaml` in both the `options` section (with default value and comment)
  - Add to `config.yaml` in the `schema` section (with proper validation)
  - Add to `translations/en.yaml` with name and description
- If new parameters are found, ensure they are properly documented

## Step 3: Extract Version Information

- Get the most recent commits from the submodule
- Find the latest `[AUTO]` version update commit (format: "Update version to X.X.X.XXX-develop")
- Extract the version number from that commit message
- The version format is: MAJOR.MINOR.PATCH.BUILD (e.g., 0.2.29.208)

## Step 4: Update config.yaml

- Update the version field in `eos_connect_develop\config.yaml`
- Remove the "-develop" suffix from the version (e.g., 0.2.29.208-develop becomes 0.2.29.208)

## Step 5: Update CHANGELOG.md

- Add a new entry at the TOP of `eos_connect_develop\CHANGELOG.md` (before any existing entries)
- Format: `**Version X.X.X.XXX** published on YYYY-MM-DD`
- For EACH non-AUTO commit since the last eos_connect_develop parent repo commit:
  - Add a bullet point with the commit message
  - If the commit message contains "fixes" or "Fixes #XXX", include the issue reference
  - Preserve the original formatting (issue links, descriptions)
  - Skip commits with `[AUTO]` prefix

## Entry Format Example:

```
**Version 0.2.29.208** published on 2025-12-15
- Enhance discharge state handling by introducing effective discharge logic and updating related MQTT topics to reflect final states after overrides - fixes Missing State in HA for Allow Discharge EVCC
Fixes [#175](https://github.com/ohAnd/EOS_connect/issues/175)
- Implement dynamic max charge power based on charging curve configuration in get_pv_akku_data function - fixes part 2 of evopt lädt zu wenig/langsam
Fixes [#167](https://github.com/ohAnd/EOS_connect/issues/167)
```

## Important Notes:

- Skip commits with `[AUTO]` prefix in the commit message (these are automatic version bumps)
- Each feature/fix from the actual commits gets its own bullet point
- Preserve GitHub issue links in the format `[#XXX](https://github.com/ohAnd/EOS_connect/issues/XXX)`
- Use the current date for the "published on" field
- Multiple related changes from one commit should be on separate bullet points if they are logically distinct
- When a commit has "Fixes #XXX" in the message, put it on a separate line

## Step 6: Show Proposed Commit Message

- After completing all updates, display the proposed commit message for the user to review
- Commit message format: `eos_connect_develop: bump version to X.X.X.XXX; update changelog with [brief summary of changes]; modify config.yaml for version update`
- Brief summary should mention the key features/fixes (e.g., "discharge state handling and dynamic max charge power")
- DO NOT automatically commit - let the user review and commit manually

### Mandatory confirmation step

- After showing the proposed commit message the agent MUST wait for the human to send the exact phrase `approve eos commit` before performing any `git commit` or `git push`.
- If the human responds with anything else, the agent must NOT commit and should instead ask for clarification or update the proposed commit message as requested.

### Staging behaviour

- The agent should list staged files and may stage changes, but MUST NOT commit/push without the exact confirmation phrase.

### Audit and reporting

- The agent must include the extracted version number and the list of non-[AUTO] commit messages used to populate `CHANGELOG.md` in the confirmation request.

## Important: Enforcement recommendation

- To help ensure these rules are respected by any automated agent, create a repository-level git hook or CI check which blocks commits unless an environment variable `ALLOW_BOT_COMMIT=true` is explicitly set by a human step. This instructions file defines the expected behaviour but cannot enforce it without repository hooks or CI.
