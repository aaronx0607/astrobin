/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.5
 * 
 * This file is not intended to be easily readable and contains a number of 
 * coding conventions designed to improve portability and efficiency. Do not make
 * changes to this file unless you know what you are doing--modify the SWIG 
 * interface file instead. 
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_Xapian_WRAP_H_
#define SWIG_Xapian_WRAP_H_

class SwigDirector_PostingSource : public Xapian::PostingSource, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_PostingSource(JNIEnv *jenv);
    virtual ~SwigDirector_PostingSource();
    virtual Xapian::doccount get_termfreq_min() const;
    virtual Xapian::doccount get_termfreq_est() const;
    virtual Xapian::doccount get_termfreq_max() const;
    virtual Xapian::weight get_weight() const;
    virtual Xapian::docid get_docid() const;
    virtual void next(Xapian::weight min_wt);
    virtual void skip_to(Xapian::docid did, Xapian::weight min_wt);
    virtual bool check(Xapian::docid did, Xapian::weight min_wt);
    virtual bool at_end() const;
    virtual Xapian::PostingSource *clone() const;
    virtual std::string name() const;
    virtual std::string serialise() const;
    virtual Xapian::PostingSource *unserialise(std::string const &s) const;
    virtual void init(Xapian::Database const &db);
    virtual std::string get_description() const;
public:
    bool swig_overrides(int n) {
      return (n < 12 ? swig_override[n] : false);
    }
protected:
    bool swig_override[12];
};

class SwigDirector_MatchDecider : public Xapian::MatchDecider, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_MatchDecider(JNIEnv *jenv);
    virtual bool operator ()(Xapian::Document const &doc) const;
    virtual ~SwigDirector_MatchDecider();
public:
    bool swig_overrides(int n) {
      return (n < 1 ? swig_override[n] : false);
    }
protected:
    bool swig_override[1];
};

class SwigDirector_ExpandDecider : public Xapian::ExpandDecider, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_ExpandDecider(JNIEnv *jenv);
    virtual bool operator ()(std::string const &term) const;
    virtual ~SwigDirector_ExpandDecider();
public:
    bool swig_overrides(int n) {
      return (n < 1 ? swig_override[n] : false);
    }
protected:
    bool swig_override[1];
};

class SwigDirector_MatchSpy : public Xapian::MatchSpy, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_MatchSpy(JNIEnv *jenv);
    virtual ~SwigDirector_MatchSpy();
    virtual void operator ()(Xapian::Document const &doc, Xapian::weight wt);
    virtual Xapian::MatchSpy *clone() const;
    virtual std::string name() const;
    virtual std::string serialise() const;
    virtual Xapian::MatchSpy *unserialise(std::string const &s, Xapian::Registry const &context) const;
    virtual std::string serialise_results() const;
    virtual void merge_results(std::string const &s);
    virtual std::string get_description() const;
public:
    bool swig_overrides(int n) {
      return (n < 4 ? swig_override[n] : false);
    }
protected:
    bool swig_override[4];
};

class SwigDirector_Stopper : public Xapian::Stopper, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_Stopper(JNIEnv *jenv);
    virtual bool operator ()(std::string const &term) const;
    virtual ~SwigDirector_Stopper();
    virtual std::string get_description() const;
public:
    bool swig_overrides(int n) {
      return (n < 2 ? swig_override[n] : false);
    }
protected:
    bool swig_override[2];
};

struct SwigDirector_ValueRangeProcessor : public Xapian::ValueRangeProcessor, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_ValueRangeProcessor(JNIEnv *jenv);
    virtual ~SwigDirector_ValueRangeProcessor();
    virtual Xapian::valueno operator ()(std::string &begin, std::string &end);
public:
    bool swig_overrides(int n) {
      return (n < 1 ? swig_override[n] : false);
    }
protected:
    bool swig_override[1];
};

struct SwigDirector_StemImplementation : public Xapian::StemImplementation, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_StemImplementation(JNIEnv *jenv);
    virtual ~SwigDirector_StemImplementation();
    virtual std::string operator ()(std::string const &word);
    virtual std::string get_description() const;
public:
    bool swig_overrides(int n) {
      return (n < 2 ? swig_override[n] : false);
    }
protected:
    bool swig_override[2];
};

class SwigDirector_KeyMaker : public Xapian::KeyMaker, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_KeyMaker(JNIEnv *jenv);
    virtual std::string operator ()(Xapian::Document const &doc) const;
    virtual ~SwigDirector_KeyMaker();
public:
    bool swig_overrides(int n) {
      return (n < 1 ? swig_override[n] : false);
    }
protected:
    bool swig_override[1];
};

class SwigDirector_Compactor : public Xapian::Compactor, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_Compactor(JNIEnv *jenv);
    virtual ~SwigDirector_Compactor();
    virtual void set_status(std::string const &table, std::string const &status);
    virtual std::string resolve_duplicate_metadata(std::string const &key, size_t num_tags, std::string const tags[]);
public:
    bool swig_overrides(int n) {
      return (n < 2 ? swig_override[n] : false);
    }
protected:
    bool swig_override[2];
};


#endif
