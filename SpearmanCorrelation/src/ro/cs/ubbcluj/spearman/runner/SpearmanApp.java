package ro.cs.ubbcluj.spearman.runner;

import java.util.stream.Collectors;
import java.util.stream.Stream;

import javax.sound.midi.Soundbank;

import ro.cs.ubbcluj.domain.Entity;
import ro.cs.ubbcluj.domain.SpearmanCoefficient;
import ro.cs.ubbcluj.domain.Variable;

public class SpearmanApp {

	public static void main(String[] args) {
		Stream<Integer> stream = Stream.of(56, 75, 45, 71, 61, 64, 58, 80, 76, 61);
		Entity<Integer> englishGrades = new Variable(stream.collect(Collectors.toList()));

		Stream<Integer> stream2 = Stream.of(66, 70, 40, 60, 65, 56, 59, 77, 67, 63);
		Entity<Integer> mathGrades = new Variable(stream2.collect(Collectors.toList()));

		SpearmanCoefficient spearman = new SpearmanCoefficient(englishGrades.getFeatureList().size(), englishGrades,
				mathGrades);

		System.out.println(englishGrades.computeRanks());
		System.out.println(mathGrades.computeRanks());
		if (!englishGrades.hasTiedRanks() && !mathGrades.hasTiedRanks()) {
			System.out.println(spearman.computeSpearmanWithoutTiedRanks());

		}
		else{
			System.out.println(spearman.computeSpearmanWithTiedRanks());
		}
	}

}
