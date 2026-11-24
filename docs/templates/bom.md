# Bill of Materials

Every part in the build, what it costs, what's left to buy, and when it arrives. You fill in the white columns; the gray ones calculate themselves.

**Version 1.0.0**

<!-- The release step fills in these two links. -->
[Make a copy (Google Sheets)](https://docs.google.com/spreadsheets/d/RELEASE_SHEET_ID/copy){ .md-button .md-button--primary } [Download .xlsx](https://github.com/syseng-toolkit/syseng-toolkit.github.io/releases/tag/bom-v1.0.0){ .md-button }

## Tabs

| Tab | What it's for |
|---|---|
| BOM | One row per part, kept forever. |
| Dashboard (READ ONLY) | Build cost, spend, cost left to buy, breakdown by subsystem and status, and what's on order. |
| Delivery Timeline (READ ONLY) | Day-by-day chart of every order, from order to arrival, in BOM order. |
| Shopping List (READ ONLY) | Everything still to buy, grouped by supplier, with packs and cost. |
| Document Release | Official versions of your BOM, for example at a build review. |
| Lists | Dropdown values (subsystem, bought by). |
| Template History | Release notes for this template. The last row is the version your copy is on. |

## How cost works

- **Pack Price / Pack Size:** what you actually pay and how many come in it ($9.50 for 100 screws). Leave Pack Size blank for single items.
- **Build Cost** = Qty / Build × unit cost: what one build costs. Leaves out spares and leftover pieces.
- **Spent** = Packs Ordered × Pack Price: real money out the door, including leftovers and obsolete parts.
- **Packs to Buy:** packs still needed to cover Qty / Build + Spares, rounded up to whole packs. Feeds the Shopping List.

## Status and Next Step

Status is worked out from the quantities, against **Total Need** (Qty / Build + Spares):

| Status | Meaning |
|---|---|
| Need to order | Pieces ordered don't cover Total Need yet. |
| Ordered | Enough is ordered. |
| Partial | Some has arrived. |
| Received | Qty Received covers Total Need. |
| Obsolete | The Obsolete box is ticked. The row keeps its part number and stays in Spent, but drops out of Build Cost and the Shopping List. |

**Next Step** says in plain English what to do: how many more to buy, from which supplier and for how much, the order-by date, which inputs are missing, and "past due, chase <supplier>" once an expected delivery is late. It turns red when something is late.

## Day to day

- **Ordering:** enter Packs Ordered and Order Date. Status flips to Ordered when the packs cover Total Need.
- **Receiving:** enter Qty Received and Date Received (the latest arrival, for partial deliveries).
- **Planning:** enter Need By (when you need it in hand). Order By = Need By minus Lead Time, and goes red if it has passed while the part still needs ordering.
- **Delivery Timeline:** set the yellow cells at the top: Start (`=TODAY()-14` keeps it rolling), Days per column (1 = daily, 7 = weekly) and Subsystem. ◆ estimated arrival, ✓ received, ⚑ need by. Bars are red when late or landing after Need By.

## Columns

| Column | Typed or auto | What goes in it |
|---|---|---|
| Part # | Typed | `PN-####` (the next free one is on the README). Never reused. |
| Description | Typed | What the part is, specific enough to reorder (size, rating, model). |
| Subsystem | Typed (dropdown) | Which subsystem uses it. |
| Qty / Build | Typed | Pieces needed for one build. |
| Spares | Typed, optional | Extra pieces to keep on hand. Not in Build Cost. |
| Total Need (auto) | Auto | Qty / Build + Spares. Status checks against this. |
| Supplier | Typed | Where you buy it. The Shopping List groups by this. |
| Link / Supplier P/N | Typed | Product page link or the supplier's part number. |
| Pack Price | Typed | What you pay for one pack (or one item). |
| Pack Size | Typed | Pieces per pack. Blank for single items. |
| Packs Needed (auto) | Auto | Packs it takes to cover Total Need, rounded up. |
| Packs Ordered | Typed | Packs you bought. This marks a part as ordered. |
| Order Date | Typed | When you ordered. Yellow if Packs Ordered is filled without it. |
| Lead Time (days) | Typed | Typical days from order to arrival. |
| Need By | Typed | When you need the part in hand. |
| Qty Received | Typed | Pieces actually in hand. |
| Date Received | Typed | When they arrived. Yellow if Qty Received is filled without it. |
| Bought By | Typed (dropdown) | Who placed the order. |
| Obsolete | Checkbox | Tick instead of deleting the row. |
| Notes | Typed | Alternates, why this part, the requirement it serves. |
| Status (auto) | Auto | Need to order / Ordered / Partial / Received / Obsolete. |
| Next Step (auto) | Auto | What to do next, in plain English. |
| Unit Cost (auto) | Auto | Pack Price ÷ Pack Size. |
| Build Cost (auto) | Auto | Qty / Build × Unit Cost. |
| Spent (auto) | Auto | Packs Ordered × Pack Price. |
| Pieces Ordered (auto) | Auto | Packs Ordered × Pack Size. |
| Packs to Buy (auto) | Auto | Packs still to buy after Packs Ordered. |
| Cost to Buy (auto) | Auto | Packs to Buy × Pack Price. |
| Est. Arrival (auto) | Auto | Order Date + Lead Time. |
| Order By (auto) | Auto | Latest date to order and still have it by Need By. |

## Google Sheets and Excel

Everything calculates in both, including the charts and the Delivery Timeline. Google Sheets only: warning-only protection on the README and READ ONLY tabs, and the pink warning when a formula is typed over.

## Release notes

### 1.0.0

First release. Parts list (PN-####) with pack math, ordering and delivery tracking, and an automatic Status and Next Step. Dashboard, Delivery Timeline and Shopping List (READ ONLY). Document Release tab for the project's own releases.
