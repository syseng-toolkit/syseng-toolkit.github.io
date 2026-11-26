# Task Tracker

High-level tasks and milestones, run in sprints. One list for everything; the views, the dashboard and the Gantt chart build themselves.

**Version 1.0.0**

<!-- The release step fills in these two links. -->
[Make a copy (Google Sheets)](https://docs.google.com/spreadsheets/d/RELEASE_SHEET_ID/copy){ .md-button .md-button--primary target=_blank rel=noopener } [Download .xlsx](https://github.com/syseng-toolkit/syseng-toolkit.github.io/releases/tag/task-tracker-v1.0.0){ .md-button }

## Tabs

| Tab | What it's for |
|---|---|
| Dashboard (READ ONLY) | Status at a glance: overall and current-sprint counts, milestone progress, open work by owner, what needs attention, and what's due in the next 14 days. |
| Tasks | The main list. One row per task, kept forever. |
| Task View (READ ONLY) | Pick a sprint and/or a milestone in the yellow dropdowns to see just those tasks. |
| Milestones | A handful of key events (`MS-##`). Tasks link to one through their Milestone column. |
| Gantt (READ ONLY) | Built from Tasks and Milestones, grouped by milestone then start date. |
| Sprint Log | Sprint 1 start and sprint length (yellow cells), then one row per sprint: goal, done and open counts, carried over, retro notes. |
| Lists | Dropdown values (status, priority, subsystem, owner). |
| Document Release | Official versions of your plan, for example the plan agreed at a design review. |
| Template History | Release notes for this template. The last row is the version your copy is on. |

## The sprint rhythm

1. **Review.** Open the Dashboard or the Task View for the current sprint. Mark finished tasks Done and type the Completed date (Ctrl+; = today; the cell stays yellow until you do). Set Status honestly: Blocked if it's waiting.
2. **Carry over.** For each unfinished task, change Sprint to the next one (and Due if it moved). Note the count on Sprint Log.
3. **Plan.** Add tasks for the next sprint with an Owner, Priority, Start, Due and a Definition of Done, in the next empty row at the bottom.
4. **Check.** Look at the Gantt and the Dashboard: overdue (orange), blocked (red), and milestones whose Last Task Due is red.

## Rules

- **One owner per task,** even if several people help, so it's clear who's on the hook.
- **A Definition of Done is required.** If you can't say what done looks like, the task isn't ready for a sprint.
- **Don't delete tasks.** Leave them Done, or Canceled if they were dropped.
- **Status is set by people; Flag is automatic.** Flag never changes Status. It shows: Overdue · Waiting on TSK-### · Unknown ID in Depends on · Starts before a dependency is due · Should have started.
- **Paused** means on hold on purpose: still open, but no Overdue flags. **Canceled** is struck through and left out of totals, but kept for history.
- **Depends on** lists the tasks this one waits on, comma-separated (`TSK-002, TSK-004`). Deps Due shows when the last of them is due.
- **Sprints are numbers** (S1, S2…). Change Sprint 1 start or the sprint length on Sprint Log any time; tasks keep their sprints and the dates update. For work that spans sprints, also pick a Last Sprint.
- **To link a task to a requirement,** mention the `REQ-###` in Notes.

## The Gantt chart

- **Start** (yellow, B2): the first date shown. `=TODAY()-7` keeps it rolling.
- **Days per column** (yellow, D2): 1 = daily with weekends shaded, 7 = weekly; anything from 1 to 90.
- **Bars** cover Start to Due: gray done · blue in progress · light blue not started · red blocked · orange overdue · lavender paused · faint gray canceled. A task needs both Start and Due to get a bar.
- **◆** marks a milestone's target date. **▸** marks when each of a task's dependencies is due, so a bar that starts before a ▸ is starting early. **✓** marks the day a task was completed.

## Columns

### Tasks tab

| Column | Typed or auto | What goes in it |
|---|---|---|
| ID | Typed | `TSK-###`, never reused. Turns red if its row is missing formulas (made with Insert row): add tasks at the bottom instead. |
| Task | Typed | What gets done, as a short action, verb first. |
| Milestone | Typed (dropdown) | The `MS-##` this task works toward. |
| Subsystem | Typed (dropdown) | Which subsystem the work is for. |
| Owner | Typed (dropdown) | Exactly one person. |
| Priority | Typed (dropdown) | High / Medium / Low. |
| Sprint | Typed (dropdown) | The sprint it's planned for (S1, S2…). |
| Last Sprint (optional) | Typed | For work over several sprints: the last one it runs in. Red if before Sprint. |
| Sprint Dates (auto) | Auto | The sprint's dates, or the whole span for a multi-sprint task. |
| Start | Typed | Planned start date. Red if it's before a dependency is due. |
| Due | Typed | Planned finish date. Orange when passed and not Done. |
| Status | Typed (dropdown) | Not started / In progress / Blocked / Paused / Done / Canceled. |
| Completed | Typed | Date it was actually finished. Yellow = Done with no date; orange = finished after Due. |
| Flag (auto) | Auto | Heads-up only, never changes Status. |
| Definition of Done | Typed, required | How anyone can tell it's finished: a test passed, a file in the repo, a review signed off. |
| Depends on | Typed | Task IDs this one waits on, comma-separated. |
| Notes | Typed | Anything else, including the `REQ-###` the task serves. |
| Deps Due (auto) | Auto | Latest Due date among the tasks in Depends on. |

### Milestones tab

| Column | Typed or auto | What goes in it |
|---|---|---|
| ID | Typed | `MS-##`, never reused. |
| Milestone | Typed | The checkpoint, for example a demo or a design review. |
| Target Date | Typed | When it should be reached. Orange when passed and not Done. |
| Status | Typed (dropdown) | Planned / On track / At risk / Done. |
| Owner | Typed (dropdown) | One person. |
| Notes | Typed | Anything else. |
| Open Tasks (auto) | Auto | Tasks on this milestone that aren't Done or Canceled. |
| Last Task Due (auto) | Auto | Latest Due date among its tasks; red if later than Target Date. |

### Sprint Log tab

| Column | Typed or auto | What goes in it |
|---|---|---|
| Sprint (auto) | Auto | S1, S2… |
| Sprint Start (auto) | Auto | From Sprint 1 start and Sprint length (yellow cells, top right). |
| Sprint Goal (one line) | Typed | The sprint's goal, set at planning. |
| Done (auto) | Auto | Tasks done in this sprint. |
| Still Open (auto) | Auto | Tasks in this sprint not Done or Canceled. |
| Carried Over (enter at review) | Typed | How many tasks moved to the next sprint. |
| Retro Notes | Typed | What went well and what to change. |

## Google Sheets and Excel

Everything calculates in both, including the Gantt chart and the dashboard chart. Google Sheets only: warning-only protection on READ ONLY tabs, Sprint Log and Lists; the pink warning when a formula is typed over; and the red task ID for a row missing its formulas.

## Release notes

### 1.0.0

First release. Tasks (TSK-###) with one owner each, sprints, milestones (MS-##), typed dependencies and automatic flags. Task View, Gantt and Dashboard (READ ONLY). Sprint Log with the sprint start and length. Document Release tab for the project's own releases.
