// data variables must be inside parens

!!function () {
	if ((pl) > 1000 && (pc) > 1000) {
		return true;
	} else {
		return false;
	}    
}()

!!function () {
	if ( (pl) < MinPrice() ) {
		return true;
	} else {
		return false;
	}
	
	function minPrice () {
		let min = [ih][0].PriceMin;
		
		for (let i = 0; i < 21; i++) {
			if (min > [ih][i].PriceMin) {
				min = [ih][i].PriceMin;
			}
		}
		return min;
	}
}()

!!function () {
	if (typeof [ih][0].rsi == 'undefined') calcRsi(14);

	(cfield0) = [ih][0].rsi;

	return true;
	
	function calcRsi(period) {
		let len = 20;
		
		for (let i = 0; i < len; i++) {
			var rec = [ih][len - 1 - i];
			var change = rec.PClosing - rec.PriceYesterday;
			if (change > 0) {
				rec.gain = change;
				rec.loss = 0;
			} else {
				rec.gain = 0;
				rec.loss = -change;
			}
		}

		// calculate first "average gain" and "average loss"
		let gainSum = 0;
		let lossSum = 0;
		for (let i = 0; i < period; i++) {
			let rec = [ih][len - 1 - i];
			gainSum += rec.gain;
			lossSum += rec.loss;
		}

		let averageGain = gainSum / period;
		let averageLoss = lossSum / period;
		// calculate subsequent "average gain" and "average loss" values
		for (var i = period + 1; i < len; i++) {
			let rec = [ih][len - 1 - i];
			averageGain = (averageGain * (period - 1) + rec.gain) / period;
			averageLoss = (averageLoss * (period - 1) + rec.loss) / period;
			rec.averageGain = averageGain;
			rec.averageLoss = averageLoss;
		}

		// calculate rsi
		let rs = 0;    // relative strength
		let rsIndex = 0; // relative strength index
		for (var i = period + 1; i < len; i++) {
			let rec = [ih][len - 1 - i];
			rs = rec.averageGain / rec.averageLoss;
			rsIndex = 100 - 100 / (1 + rs);
			rec.rsi = rsIndex;
		}
	}
}()