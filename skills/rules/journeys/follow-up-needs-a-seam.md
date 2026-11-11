# Journey: a follow-up that needs a seam first

**The user says:** "US customers should pay in USD."
**Comes after:** [a new Feature on a strong foundation](new-feature.md), whose preparation settled "Currency: no".

```mermaid
flowchart LR
  ask[User: charge in USD] --> build[task]
  build --> spot[CAD hardcoded, no seam]
  spot --> refactor[Refactor: add the currency seam, behavior preserved]
  refactor --> feature[Feature: add USD on the seam]
  feature --> review[review]
```

## 1. Route and spot the gap

"Should pay in USD" asks for a change: open `task/SKILL.md`. Finding siblings turns up `"cad"` hardcoded in `billing.ts` and `stripe-provider.ts`, with no seam. This is a Feature that fits no seam where one should now exist ([Scale to the work](../strong-foundation.md#scale-to-the-work)).

## 2. Grill the split

```markdown
## Questions
Reply like: 1a

1. Currency is hardcoded as CAD in `billing.ts` and `stripe-provider.ts`. How should USD land?
   - a) split: first a Refactor that passes a currency through `makeUserPay` with CAD everywhere (no behavior change), then the Feature that adds USD ← recommended
   - b) add a USD branch inside `billing.ts`
```

Option b bolts a special case onto the foundation, and the third currency repeats the edit. The Locked in message repeats that rejected option.

## 3. Two builds, in order

1. **Refactor.** Remove the hardcoded value first ([keep-it-simple.md](../keep-it-simple.md#before-you-add), subtract first). `makeUserPay` takes a `currency`, and every current caller passes `"cad"`. Verify preserved behavior with relevant existing billing tests and affected caller/type checks under [verification scope](../execution.md#verification-scope). When the user requests tickets separately, `/write-ticket` makes this its own implementation ticket (kind Refactor). It ships on its own branch: `refactor/IN-57-pass-currency-through-billing`.
2. **Feature.** Now USD fits the seam: checkout picks the currency from the customer's country. `/verification` proposes one test: a US customer's payment through `makeUserPay` is charged in USD.

## 4. Review

The Refactor diff is reviewed for preserved behavior. The Feature diff passes the Foundation check: USD arrives as a value on the seam, not as an `if` in the service.

## If a step is skipped

- No split: the special case ships, and every later change must know about it.
- Refactor and Feature in one diff: review cannot tell a behavior change from a move.
