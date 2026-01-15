// a_cards_coins.js
export default {
  name: "Cards / Coins",
  description:
    "Classic puzzle: Pick the known number of heads blindly, flip them, and both piles have equal heads.",

  useVisited: false,

  // Initial state: coins numbered, some heads, some tails, not revealed yet
  initialState() {
    const totalCoins = 20;  // Total coins
    const totalHeads = 10;   // Number of heads (known)
    const coins = [];

    // Assign heads and tails
    for (let i = 1; i <= totalCoins; i++) {
      coins.push({ id: i, type: i <= totalHeads ? "H" : "T" });
    }

    // Shuffle coins (so heads are hidden)
    shuffleArray(coins);

    return {
      step: 0,       // Step of puzzle: 0=initial, 1=picked, 2=flipped, 3=done
      coins,
      knownHeads: totalHeads,
      pileA: [],
      pileB: [],
      flipped: false
    };
  },

  stateKey(s) {
    // Key is step + pile A + pile B ids
    return `${s.step}|${s.pileA.map(c => c.id).join(",")}|${s.pileB.map(c => c.id).join(",")}`;
  },

  isGoal(s) {
    return s.step === 3; // Puzzle solved
  },

  getNextStates(s) {
    const next = [];

    if (s.step === 0) {
      // Step 0 → pick K coins blindly for Pile A
      const picked = s.coins.slice(0, s.knownHeads);
      const remaining = s.coins.slice(s.knownHeads);
      next.push({
        ...s,
        step: 1,
        pileA: picked,
        pileB: remaining,
        flipped: false
      });
    } else if (s.step === 1) {
      // Step 1 → flip Pile A
      const flippedPileA = s.pileA.map(c => ({
        ...c,
        type: c.type === "H" ? "T" : "H"
      }));
      next.push({
        ...s,
        step: 2,
        pileA: flippedPileA,
        pileB: s.pileB,
        flipped: true
      });
    } else if (s.step === 2) {
      // Step 2 → goal reached
      next.push({
        ...s,
        step: 3
      });
    }

    return next;
  },

  liveExplanation(s) {
    switch (s.step) {
      case 0:
        return `Step 1: Pick ${s.knownHeads} coins blindly into Pile A.`;
      case 1:
        return `Step 2: Flip all coins in Pile A.`;
      case 2:
        return `Step 3: Both piles now have equal number of heads!`;
      default:
        return "";
    }
  },

  renderState(s, ctx) {
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    ctx.font = "18px monospace";
    ctx.fillStyle = "black";

    const startY = 200;
    const pileAY = startY;
    const pileBY = startY + 150;

    // Labels
    ctx.fillText("Pile A", 20, pileAY - 40);
    ctx.fillText("Pile B", 20, pileBY - 40);

    // Draw Pile A
    drawPile(ctx, s.pileA.length > 0 ? s.pileA : s.coins, 50, pileAY, s.step >= 2);

    // Draw Pile B
    drawPile(ctx, s.pileB.length > 0 ? s.pileB : [], 50, pileBY, s.step >= 2);

    // Show numeric heads after flipping
    if (s.step >= 2) {
      const headsA = s.pileA.filter(c => c.type === "H").length;
      const headsB = s.pileB.filter(c => c.type === "H").length;
      ctx.fillText(`Heads in Pile A: ${headsA}`, 400, pileAY);
      ctx.fillText(`Heads in Pile B: ${headsB}`, 400, pileBY);
    }
  }
};

// Helper to shuffle array
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}

// Helper to draw a pile
function drawPile(ctx, coins, startX, startY, reveal = false) {
  coins.forEach((coin, i) => {
    ctx.beginPath();
    ctx.arc(startX + i * 50, startY, 20, 0, Math.PI * 2);

    // Gray if hidden, gold for heads, light gray for tails if revealed
    if (reveal) {
      ctx.fillStyle = coin.type === "H" ? "gold" : "#ccc";
    } else {
      ctx.fillStyle = "#999"; // unknown coin
    }

    ctx.fill();
    ctx.stroke();

    // Draw coin number
    ctx.fillStyle = "black";
    ctx.fillText(coin.id, startX + i * 50 - 5, startY + 5);
  });
}
