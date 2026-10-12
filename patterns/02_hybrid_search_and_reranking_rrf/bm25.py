"""
bm25.py — Thuật toán tìm kiếm từ khóa chính xác BM25 Okapi chuẩn mực.
"""
import math
import re
from typing import List, Dict

class BM25Okapi:
    def __init__(self, corpus: List[str], k1: float = 1.5, b: float = 0.75):
        self.corpus = corpus
        self.k1 = k1
        self.b = b
        self.corpus_size = len(corpus)
        self.doc_lens = []
        self.tokenized_corpus = []
        self.doc_freqs: Dict[str, int] = {}

        for doc in corpus:
            tokens = self.tokenize(doc)
            self.tokenized_corpus.append(tokens)
            self.doc_lens.append(len(tokens))
            unique_tokens = set(tokens)
            for t in unique_tokens:
                self.doc_freqs[t] = self.doc_freqs.get(t, 0) + 1

        self.avg_doc_len = sum(self.doc_lens) / self.corpus_size if self.corpus_size > 0 else 0.0

    @staticmethod
    def tokenize(text: str) -> List[str]:
        """Tách từ đơn giản, chuyển chữ thường và xử lý mã kỹ thuật."""
        return re.findall(r"\b[\w\-]+\b", text.lower())

    def get_scores(self, query: str) -> List[float]:
        query_tokens = self.tokenize(query)
        scores = [0.0] * self.corpus_size

        for token in query_tokens:
            if token not in self.doc_freqs:
                continue
            df = self.doc_freqs[token]
            idf = math.log((self.corpus_size - df + 0.5) / (df + 0.5) + 1.0)

            for i, doc_tokens in enumerate(self.tokenized_corpus):
                tf = doc_tokens.count(token)
                if tf == 0:
                    continue
                doc_len = self.doc_lens[i]
                numerator = tf * (self.k1 + 1.0)
                denominator = tf + self.k1 * (1.0 - self.b + self.b * (doc_len / self.avg_doc_len))
                scores[i] += idf * (numerator / denominator)

        return scores
