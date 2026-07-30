---
title: Decentralised Finance - DeFi
date: 2026-07-29
tags: ["money"]
tagline: "A journey into Decentralized Finance."
---

*From "what is DeFi?" to encrypted lending vaults*

I've been hearing the term "DeFi" for years.  I've searched on it a bunch of times, and read the words, got the concepts, but never truly felt like I've understood it.  But with an LLM as my guide and a browser as my tool I seem to have made more headway this time. If you've been trying to understand DeFi, this might be for you.

---

## What Is DeFi?

**DeFi** or **decentralized finance** is a collective term for financial services — lending, borrowing, trading, earning yield — that run on blockchains via *smart contracts* instead of through banks, brokers, or other intermediaries.

The core idea is peer-to-peer finance. Instead of a bank sitting between you and the person you're lending to, a piece of code (a smart contract) enforces the rules. No credit checks. No paperwork. No business hours. No owner who can unilaterally change the terms.

Think of it this way: 
> a **blockchain** is the restaurant building — the physical space, the kitchen, the plumbing. A **protocol** is the restaurant itself — the menu, the recipes, the way the whole operation works. A **smart contract** is an individual recipe — a specific set of instructions that runs on its own. DeFi protocols are financial restaurants built inside blockchain buildings.

DeFi runs primarily on **Ethereum** (the pioneer and largest ecosystem) and **Solana** (a faster, cheaper alternative), among others. The same protocol generally can't run on both — they're different blockchains (buildings) with different architectures — which is one reason the ecosystem is so fragmented.

---

## What Are "Protocols" and Who Creates Them?

When someone says DeFi covers "hundreds of protocols," they mean hundreds of smart-contract-based financial applications (ie: restaurants). Each one was created by **developers** who wrote and deployed code on a blockchain. Control is often then transferred to **DAOs** (Decentralized Autonomous Organizations) — communities of token holders who vote on changes.

The major categories of DeFi protocols are:

| Category | What It Does | Examples |
|---|---|---|
| **DEXs / AMMs** | Decentralised exchanges and market makers to buy & sell tokens peer-to-peer | Uniswap, Curve, Jupiter, Raydium |
| **Lending & Borrowing** | Supply assets to earn interest, or borrow against collateral | Aave, Compound, Kamino, MarginFi |
| **Liquid Staking** | Deposit ETH/SOL tokens then receive a liquid token you can re-use elsewhere | Lido, Jito, ether.fi, Sanctum |
| **Stablecoins** | Crypto tokens pegged to a fiat currency (usually USD) | USDC, USDT, DAI, USDe |
| **Derivatives / Perps** | Trade futures and other derivatives onchain | Hyperliquid, Jupiter Perps, dYdX |
| **Yield Aggregators** | Automatically move deposits across strategies to maximize returns | Yearn Finance, Beefy Finance, Tulip |
| **Real-World Assets (RWA)** | Tokenized Treasuries, bonds, stocks onchain | Ondo, BlackRock BUIDL |
| **Prediction Markets** | Bet on real-world event outcomes | Polymarket |
| **Flash Loans** | Setup a chain of transactions that succeed or fail atomically (eg: take a profit or cancel the whole thing) | Aave, Balancer |

The revolutionary part is **composability** — these protocols are like Lego bricks that snap together. You can stake ETH, use the receipt token as collateral to borrow USDC, then deposit that USDC into a yield vault. Each piece is a separate protocol, but they interoperate because they're all smart contracts on the same blockchain.  You can chain deals together in new, interesting, and compounding ways.

---

## Borrowing and Lending: How It Actually Works

So can I borrow money from a DeFi protocol on Solana? Yes — but "borrow" in DeFi doesn't mean what it means at a bank.

DeFi lending is **overcollateralized**: you must deposit crypto assets worth *more* than you borrow. There's no credit check and no human approval. The smart contract enforces everything automatically.

Here's how a typical interaction works:

**As a borrower:**
1. You deposit collateral — say, 5 ETH (~$15,000).
2. The protocol assigns a collateral factor (e.g., 80%), so you can borrow up to $12,000.
3. You borrow USDC from the pool. Interest accrues.
4. If your collateral value drops below a threshold, the protocol **automatically liquidates** your position — selling your ETH to repay the loan plus a penalty. No margin call. No warning. It just happens.

**As a lender (investor):**
1. You deposit, say, $10,000 USDC into a lending pool.
2. You receive interest-bearing receipt tokens (e.g., "aUSDC" on Aave) that accrue interest automatically.
3. You earn yield from the interest that borrowers pay. No lock-up — withdraw anytime (subject to available liquidity).

### The most common lending protocol: Aave

**Aave** is the largest and most battle-tested DeFi lending protocol, running since 2020 on Ethereum and many EVM-compatible chains (Arbitrum, Base, Optimism, Polygon, and others). It's been audited by multiple top security firms, uses formal verification, and has a Safety Module (a staked reserve that can cover shortfall events). On Solana, the equivalents are Kamino, MarginFi, Save (formerly Solend), and Jupiter Lend.

### Current yields (as of late July 2026)

On Aave's Ethereum market, USDC supply rates were around **3.15% APR**, with a 30-day average of ~3.4%. Rates on Layer-2 chains (Arbitrum, Base) tend to be higher due to more leveraged trading activity. These are **variable rates** — they fluctuate with borrowing demand. In periods of high demand, they've been as high as 15%+; during quiet periods, they settle toward 3–5%.

---

## What About Security? Can You Lose Your Money?

This is the question that matters most, and the honest answer is: **yes, you can.**

DeFi operates in a "trust the code" paradigm. Your security depends entirely on the correctness of smart contracts and the honesty of price feeds. There is **no mandatory insurance, no government protection, no central authority guaranteeing your funds.**

### The main risks

| Risk | What It Means |
|---|---|
| **Smart contract bugs** | A flaw in the code can let an attacker drain the entire pool. This is the #1 risk. |
| **Oracle manipulation** | If an attacker manipulates the price feeds a protocol relies on, they can borrow more than collateral is worth or trigger false liquidations. |
| **Liquidation risk** (borrowers) | If your collateral value drops, the protocol auto-liquidates with a penalty. You can lose part of your deposit. |
| **Governance attacks** | If governance tokens are concentrated, a malicious actor could vote to change the rules. |

### How real is the hacking threat?

Very real. In 2024, approximately $2.2 billion was stolen across crypto hacks. In 2025, that figure reached ~$3.4 billion. Across 2024–2025, there were 191 publicly known hacks moving a combined $4.67 billion in stolen value, with DeFi protocols accounting for 171 of those incidents.

The encouraging trend: despite total value locked in DeFi growing, hack losses have been suppressed relative to TVL
(Total Value Locked - total amount of money in the protocol/restaurant), suggesting improved security practices. Audits, bug bounties, and nascent DeFi insurance (like Nexus Mutual) all help — but none are guarantees.

> **The bottom line:** Overcollateralization protects the *protocol*, not you. If a protocol is hacked, you can lose everything, and there is often no recourse.

---

## Earning Yield: Yearn, Beefy, and the Ghost Town of Tulip

What are *yield aggregators*?  Protocols that automatically move your deposits across strategies to maximize returns. Here's what I found when I looked at three of them:

### Yearn Finance (Ethereum) — ~$227M TVL

Yearn has 30 tracked vaults with live APY (Annual Percentage Yield/interest rate) data. Rates range from **0.10% to 9.49%** (7-day average APY). The best stablecoin vaults earn 7–9.5%; typical stablecoin vaults earn 3–5%. Yearn is the most battle-tested aggregator and also the most conservative. It recently launched yvUSD, a zero-fee, cross-chain stablecoin vault running 9 active strategies.

### Beefy Finance (Multichain: 20+ chains) — ~$109M TVL

Beefy tracks 249 stablecoin pools alone. The top stablecoin vault was showing **26.88% APY** — but on a very small pool ($0.18M TVL) reliant on temporary token incentives. More typical mainstream stablecoin vaults earn **5–12%**. Beefy's displayed APY is net of fees (most vaults charge a 4.5% performance fee). Its multichain presence is a major advantage.

### Tulip Protocol (Solana) — effectively dormant

Tulip was Solana's first yield aggregator (launched April 2021 as SolFarm) and was innovative for its time. But by 2026, it's essentially a ghost town: **$4,637 total TVL**, a token price of $0.0124 (down from highs over $500), and a 30-day TVL decline of 16.7%. It's been completely eclipsed by Kamino, Jito, MarginFi, and others. If you want Solana yield today, Tulip is not the answer.

> **Key lesson:** Higher APYs generally correlate with higher risk — through newer/less-audited contracts, smaller liquidity, or reliance on temporary incentive tokens that could lose value. A vault showing 26% today might show 5% next week.

---

## So Why Do People Invest in DeFi At All?

If the yields are sometimes comparable to traditional products and the risks are perceptually higher, why does anyone bother? The answer is that DeFi's value goes well beyond headline APY:

**1. Yields that are genuinely higher than local banking.** For billions of people around the world (ie those with awful regional banking systems), the comparison isn't "DeFi 5% vs. Bank 5%." It's "DeFi 5% vs. savings account 0.01%."

**2. Permissionless access.** No account application, no credit check, no minimum balance, no geographic restriction. Anyone with an internet connection and a wallet can participate. For the 1.4 billion unbanked people worldwide, this isn't a marginal improvement — it's the difference between access and no access.

**3. Self-custody.** You hold the keys. Your assets aren't held by a bank that could fail or a government that could impose capital controls. (The trade-off: you bear the technical risk of losing your keys or the smart contract having a bug.)

**4. Composability.** Protocols snap together like Lego bricks. You can build financial strategies that are literally impossible in traditional finance — like flash loans (zero-collateral loans repurchased in the same transaction) or stacking staking yield + lending yield + vault yield on the same capital.

**5. 24/7 global markets.** No business hours. No settlement delays. Instant execution. Transparent pricing visible to anyone.

**6. Novel asset classes.** Tokenized yield trading, on-chain credit markets, decentralized perpetuals, and tokenized real-world assets (U.S. Treasuries onchain, accessible globally).

**7. Speculative upside.** Many DeFi users hold governance tokens that can appreciate dramatically — something a savings account doesn't offer.

The honest caveat: the OECD has found that in many emerging markets, DeFi participation today is "largely driven by speculative forces and fear of missing out, rather than practical use-cases." The potential is real; the current reality is more mixed than advocates claim.

---

## Lido stETH: The Foundational "Money Lego"

I know about ETHereum, but what is **stETH**? — a *liquid* staking token issued by the **Lido protocol**, the largest liquid staking protocol on Ethereum with ~$18–22 billion in assets under management.

### The problem it solves

Ethereum runs on Proof of Stake. To secure the network, validators must lock up at least 32 ETH (~$60,000+) as collateral and run validator infrastructure. In return, they earn staking rewards. But staked ETH is **locked** — you can't use it to trade or as collateral or otherwise employ via DeFi.

### What Lido does

Lido pools deposits from many users (any amount, even 0.01 ETH) and runs professional validators on their behalf. You deposit ETH, and Lido gives you **stETH** at a 1:1 rate. stETH is **liquid** — you can trade it, use it as collateral in Aave, provide it as liquidity in AMM pools, or restake it via EigenLayer — all while still earning Ethereum staking rewards.

### How yield shows up

stETH is a **rebasing token** — every day at 12:00 UTC, your stETH balance automatically increases as staking rewards are distributed. You wake up with more tokens; no transaction needed.

For DeFi integrations (which can't handle daily-changing balances), there's **wstETH (Wrapped stETH)** — a non-rebasing version where your token balance stays fixed but each token becomes worth more over time.

### Current yield

The base staking yield is approximately **2–3% APY** (net of Lido's 10% protocol fee). Lido's homepage shows a higher figure (~5.3%) that may include additional DeFi integration opportunities. These are estimates, not guarantees, and fluctuate with network conditions.

### The composability magic

```
1. Deposit ETH into Lido → receive stETH (earning ~2-3% staking yield)
2. Supply stETH to Aave as collateral (earn additional lending yield)
3. Borrow USDC against it
4. Deploy USDC in a yield vault (earn additional vault yield)

Total stacked yield: potentially 8-17%+
```

This is why stETH is the most widely integrated liquid staking token in DeFi — it's the foundational building block that makes composability work.

---

## The Frontier: Steakhouse Confidential Prime USDC

This is where things got real. I picked a vault at random/caught my eye. This one called **"Steakhouse Confidential Prime USDC"** on Vaults.fyi that was only 37 days old, showed transactions of "0 ETH," and offered ~8–11% APY. Here's what I learned:

### The three-party stack

| Layer | Entity | Role |
|---|---|---|
| **Curation / risk strategy** | Steakhouse Financial | Decides which lending markets to allocate deposits into; manages risk and rebalances. The largest vault curator on Morpho with $2.1B+ TVL across 48 vaults. |
| **Lending infrastructure** | Morpho (V2) | Provides the smart contracts — vaults deposit USDC into Morpho lending markets where borrowers post collateral. |
| **Confidentiality / encryption** | Zama | Provides Fully Homomorphic Encryption (FHE) that keeps individual deposit amounts and balances encrypted onchain. |

### What it does

You deposit USDC (specifically, "Confidential USDC" or **cUSDC**), and Steakhouse allocates it across Morpho lending markets where borrowers post blue-chip collateral (cbBTC, WBTC, wstETH) and pay interest. That interest flows back to depositors as yield. It's an ERC-4626 vault — you deposit cUSDC, receive **steakcUSDC** shares, and the share value appreciates over time.

### Why it's "Confidential"

In normal DeFi, every transaction is fully visible onchain. Anyone can see exactly how much you deposited and your current balance. For institutional capital — banks, funds, treasury managers — this is a dealbreaker.

This vault uses **Fully Homomorphic Encryption (FHE)**, powered by Zama. FHE is a cryptographic breakthrough that allows computation on encrypted data *without decrypting it*. The smart contract can calculate interest, process withdrawals, and manage allocations — all while the actual amounts remain encrypted. Your individual position is invisible to the public, but the total supply of the vault is auditable (you can verify the vault is solvent, just not who deposited how much).

### The "0 ETH" transactions explained

The vault deals in **cUSDC** (an encrypted token), not ETH. No ETH is ever transferred, so the ETH "value" field is naturally 0. And because cUSDC amounts are encrypted, the actual quantity being deposited can't be displayed in plaintext. The "$0" you see isn't a bug — it's the encryption working as designed. The ~$26M TVL is real and auditable at the aggregate level.

### Current yield and the 12-week incentive

The vault was showing **~8–11% APY**, but this is boosted by a **12-week incentive program** funded by **Zama** (the company behind the FHE technology). The native yield from Morpho lending is roughly **4% annually**; the rest comes from temporary boost rewards that decline over three phases and end around September 15, 2026. After that, the APY will likely drop toward the ~4% base rate.

Why is Zama paying for this? Because this is the **first real-world product** built on their confidential computing infrastructure. They need to bootstrap adoption, prove the concept works at scale, and attract institutional capital. It's a classic DeFi liquidity-mining strategy: subsidize early users to establish product-market fit.

---

## The Danger: What Happens When Incentives End?

This is the question that ties everything together, and it's the one that made me most cautious.

### The "mercenary capital" problem

When incentive programs end, a large fraction of the capital attracted by the boost typically leaves — and it leaves fast. The data is striking:

> Protocols spent over $500M on liquidity incentives in 2024–2025. Between 40% and 70% of that TVL left within 30 days of emission reductions. This is not a failure of individual programs. It is a structural feature of how DeFi incentives work.

Much of the capital in incentive-boosted vaults is **"mercenary"** — it's there only for the boosted yield, operated by sophisticated yield farmers and bots who constantly rotate capital. When the boost ends, they move to the next opportunity.

### Can this create a liquidity crunch? Yes.

In lending vaults (like Steakhouse/Morpho), your USDC isn't sitting idle — it's been **borrowed** by someone. When you want to withdraw, the vault needs to get USDC back from:

- Available idle liquidity (deposits not currently borrowed)
- Borrower repayments
- Liquidations (if a borrower's collateral drops)

If a large fraction of depositors try to withdraw simultaneously and most of the USDC is currently borrowed, there may not be enough idle liquidity to process all withdrawals immediately. Morpho's own documentation is explicit:

> *"There is a risk that all liquidity is borrowed. In this case, you might not be able to withdraw your assets right away. Instead, you will have to wait until new liquidity is available."*

### This actually happened: Aave's 2025–2026 "bank run"

This isn't theoretical. Aave — the most battle-tested DeFi lending protocol — experienced a massive wave of withdrawals described as a "DeFi bank run." It processed **$8.45 billion in withdrawals** and survived, but some users **could not withdraw immediately** because available liquidity was exhausted in certain markets. The event revealed a structural liquidity mismatch: deposits are demand-withdrawable, but the underlying loans are not demand-repayable.

Unlike traditional bank runs, there are no withdrawal queues or banking hours. Capital moves instantly, compressing what used to take days into minutes — which can make the crunch more acute, not less.

### The worst case: bad debt

Morpho's documentation warns:

> *"There could be circumstances in which the collateral's value for a position drops below the borrowed amount before liquidators can close the position. In such cases, the borrower holding this position has no incentive to repay the debt."*

If a mass withdrawal event coincides with a market crash, the vault could end up with **bad debt** — loans where the collateral isn't worth enough to repay. Remaining depositors absorb the loss, and your vault shares could be worth less than $1.

---

## But What About Criminals? Permissionless ≠ Lawless

A natural question when you hear "permissionless" is: *doesn't that make DeFi a haven for money laundering and criminal proceeds?*

**Criminals do use DeFi, but far less than you'd think — and vastly less than they use traditional finance.**

### The numbers in context

| | Traditional Finance | Cryptocurrency |
|---|---|---|
| **Annual money laundering** | **$800 billion – $2 trillion** (2–5% of global GDP) | **$158 billion** (2025, all illicit crypto flows) |
| **Illicit as % of total volume** | 2–5% of global GDP | **~1.2%** of all crypto transaction volume |

Traditional finance launders an estimated **5–13x more** money than all of crypto combined.

### How criminals actually use DeFi

Most crypto crime does **not** happen in DeFi. It happens through **centralized exchanges with weak KYC**, **stablecoin transfers** (84% of illicit crypto volume), and **OTC brokers** that convert crypto to fiat.

DeFi's specific role is **chain-hopping** — using DEXs (like Uniswap) and cross-chain bridges to swap tokens and jump between blockchains to break the investigative trail. It's a tool for the *obfuscation* step, not the storage step.

### Why DeFi isn't actually a criminal's paradise

The fundamental paradox: **traditional money laundering relies on secrecy; crypto puts every transaction on a permanent public ledger.**

- Every swap, deposit, and transfer is **publicly traceable** forever
- Blockchain analytics firms (Chainalysis, TRM Labs, Elliptic) can follow funds across chains in real-time
- The **off-ramp to fiat** is a regulated choke point — you can't buy groceries with crypto, so criminals eventually have to pass through a bank or exchange with KYC (Know Your Customer - an identity)
- Major enforcement actions are escalating: sanctioned exchanges shut down, new stablecoin regulations (the GENIUS Act, 2025), and international coordination

### The bottom line

DeFi's permissionless nature makes it useful for **one specific step** in the laundering pipeline — obfuscation through DEXs and bridges. But the actual **storage of criminal proceeds** still happens primarily in traditional finance, with its shell companies, cash couriers, and jurisdictions with weak oversight.

The real haven for crime money isn't DeFi. It's the same banking system that's been laundering $800 billion to $2 trillion a year for decades.

*See the full analysis with sources above, or explore further at [Chainalysis](https://www.chainalysis.com), [TRM Labs](https://www.trmlabs.com), and the [UNODC](https://www.unodc.org).*

---

## What I Learned: A Framework for Evaluating DeFi Yield

After this whole journey, here's the mental model:

### The essential questions

1. **What's the base yield vs. the boosted yield?** Is the APY I'm seeing coming from organic activity (borrowers paying interest) or from temporary token incentives? If incentives, when do they end, and what happens to the rate when they do?

2. **Who is paying the incentive, and why?** If someone is subsidizing your yield, they have a reason — usually bootstrapping adoption. That's fine, but understand that the subsidy is temporary and the funder's interests may not align with yours long-term.

3. **What's the liquidity profile?** Can I actually withdraw when I want to? What happens if everyone tries to withdraw at once? Is the vault's utilization (percentage of deposits currently borrowed) high?

4. **What are the layers of risk?** Every protocol stacked on top of another adds another layer of smart contract risk. The Steakhouse Confidential vault, for example, has three: Morpho + Steakhouse's curation logic + Zama's FHE encryption.

5. **Is there insurance or a safety net?** Most likely, no. And if there is, it's limited and discretionary. Assume you are on your own.

6. **Am I sizing this appropriately?** Only deposit what you can afford to have potentially illiquid for weeks. Don't put your rent money in a DeFi lending vault.

### The fundamental truth

DeFi lending has a structural mismatch: **your deposit is demand-withdrawable, but the underlying loans are not demand-repayable.** That mismatch is the vulnerability — and incentive program endings are exactly the kind of coordinated event that triggers it.

DeFi is powerful, genuinely innovative, and in some cases life-changing for people who lack access to traditional finance. But it is not a free lunch. The yields come with risks that traditional products don't carry. Don't *invest* money you can't afford to lose.  The difference between investing and gambling is measured in risk.

---

## Quick Reference: Key Terms

| Term | Meaning |
|---|---|
| **DeFi** | Decentralized finance — financial services via smart contracts on blockchains |
| **Protocol** | A system of smart contracts implementing a financial service |
| **Smart contract** | Self-executing code deployed on a blockchain |
| **Blockchain / L1** | The underlying network (Ethereum, Solana) that protocols are deployed on |
| **USDC** | USD Coin — a dollar-backed stablecoin issued by Circle (1 USDC = $1 USD) |
| **APY** | Annual Percentage Yield — annualized return including compounding |
| **TVL** | Total Value Locked — total assets deposited in a protocol |
| **Overcollateralized** | You must deposit collateral worth more than you borrow |
| **Liquidation** | Automatic sale of collateral when its value drops below a threshold |
| **Liquid staking** | Staking assets while receiving a liquid, DeFi-usable receipt token (e.g., stETH) |
| **FHE** | Fully Homomorphic Encryption — computation on encrypted data without decrypting it |
| **Composability** | The ability to chain DeFi protocols together ("money Legos") |
| **Mercenary capital** | Capital that enters only for incentive boosts and exits when they end |
| **ERC-4626** | A standard for tokenized yield-bearing vaults |
| **DAO** | Decentralized Autonomous Organization — token-holder governance |

---

*This article reflects my personal learning journey as of late July 2026. DeFi is a fast-moving space — protocols, yields, and risks change constantly. Nothing here is financial advice. Always do your own research, and never invest more than you can afford to lose.*
